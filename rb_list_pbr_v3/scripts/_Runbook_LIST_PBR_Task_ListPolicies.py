
# VARIABLE DECLARATION
TENANT_TAG = '@@{tenant_tag}@@'
minimum_priority = '@@{minimum_priority}@@'


# AUTHENTICATION
username_calm = "@@{username_calm}@@"
password_calm = "@@{password_calm}@@"
calm_ip = "https://{}:9440".format("@@{ip_calm}@@")
calm_login = (calm_ip, username_calm, password_calm)

username_pc = "@@{username_pc}@@"
password_pc = "@@{password_pc}@@"
pc_ip = "https://{}:9440".format("@@{ip_pc}@@")
pc_login = (pc_ip, username_pc, password_pc)


# STANDARD HELPER FUNCTIONS
def make_http_request(endpoint, method="GET", auth="BASIC", payload=None, username="", secret="", nutx_session_token=None, silence_errors=False):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    if nutx_session_token:
        headers["Cookie"] = "NTNX_IGW_SESSION={}".format(nutx_session_token)
        response = urlreq(endpoint, verb=method, params=payload, verify=False, headers=headers)
    else:
        response = urlreq(endpoint, verb=method, auth=auth, user=username, passwd=secret, params=payload, verify=False, headers=headers)
    print("REST elapsed total time: " + str(response.elapsed.total_seconds()))  
    print ("status code: " + str(response.status_code))
    print ("Response: " + response.text)

    if not silence_errors and not response.ok:
        print(response.json())
        response.raise_for_status()

    return response.json()


# Standard function to get a proxy token for a specified Nutanix user
def get_proxy_token(login_tuple, proxy_username):
    username, secret = login_tuple[1], login_tuple[2]
    proxy_url = login_tuple[0] + '/api/nutanix/v3/proxy_login'

    payload = { "proxy_for_username": proxy_username }
    response = make_http_request(proxy_url, method='POST', payload=json.dumps(payload), username=username, secret=secret)

    token = response['ntnx_igw_session']
    return token


# Standard function to be used to call all Nutanix v3 GET APIs
def ntnx_v3_api_get(login_tuple, api_extension, proxy_username=None, silence_errors=False):
    username, secret = login_tuple[1], login_tuple[2]
    api_url = login_tuple[0] + api_extension

    if proxy_username:
        token = get_proxy_token(login_tuple, proxy_username)
        return make_http_request(api_url, nutx_session_token=token, silence_errors=silence_errors)
    else:
        return make_http_request(api_url, username=username, secret=secret, silence_errors=silence_errors)


# Standard function to be used to call all Nutanix v3 POST APIs
def ntnx_v3_api_post(login_tuple, payload, req_method="POST", api_extension=None, length=250, filter=None, proxy_username=None, silence_errors=False):
    username, secret = login_tuple[1], login_tuple[2]

    # convert to standard list entity URL if no override provided
    if api_extension:
        api_url = login_tuple[0] + api_extension
    else:
        api_url = login_tuple[0] + '/api/nutanix/v3/{}s/list'.format(payload)

    # convert data type into the default payload for listing if the "payload" provided is a string
    if isinstance(payload, str):
        payload = {'kind': payload, 'length': length}

    # insert optional filter into payload
    if filter:
        payload['filter'] = filter

    # if payload is empty, ensure it is an empty dictionary
    if not payload:
        payload = {}

    if proxy_username:
        token = get_proxy_token(login_tuple, proxy_username)
        return make_http_request(api_url, method=req_method, payload=json.dumps(payload), nutx_session_token=token, silence_errors=silence_errors)
    else:
        return make_http_request(api_url, method=req_method, payload=json.dumps(payload), username=username, secret=secret, silence_errors=silence_errors)


# Returns a case-insensitive regex string for a given keyword, compatible with Nutanix FIQL filters
def get_case_insensitive_filter(string):
    output = ''
    for letter in string:
        output += '[{}|{}]'.format(letter.upper(), letter.lower())    
    return output


# CUSTOM HELPER FUNCTIONS
def generate_address_payload(address):
    if not address or address.upper() == 'ANY':
        return { "address_type": "ALL" }
    else:
        ip, prefix = address.split('/')
        return {
            "ip_subnet": {
                "ip": ip,
                "prefix_length": int(prefix)
           }
        }


def generate_ports_payload(ports):
    if not ports or ports.upper() == 'ANY':
        return None

    port_range_list = []
    ports = ports.split(',')
    for port in ports:
        start_end_ports = port.strip().split('-')

        # start and end ports must be same even if only one port is specified
        port_range_list.append( {
            "start_port": int(start_end_ports[0]),
            "end_port": int(start_end_ports[-1])
        } )
    
    return port_range_list


def generate_pbr_payload_base(priority, source, destination, action, vpc_uuid):
    return {
        "spec": {
            "name": "Policy with priority{}".format(priority),
            "resources": {
                "priority": int(priority),
                "source": generate_address_payload(source),
                "destination": generate_address_payload(destination),
                "action": { "action": action },
                "vpc_reference": {
                    "kind": "vpc",
                    "uuid": vpc_uuid
                }
            }
        },
        "metadata": { "kind": "routing_policy" }
    }


def add_protocol_details(base_payload, protocol, source_ports, destination_ports, icmp_type, icmp_code, number_protocol):
    protocol = protocol.upper()
    protocol_parameters = {}

    # Handle different protocol cases
    if protocol == 'ANY':
        protocol = 'ALL'

    elif protocol in ['TCP', 'UDP']:
        tcp_udp_parameters = {}
        source_port_range_list = generate_ports_payload(source_ports)
        destination_port_range_list = generate_ports_payload(destination_ports)

        if source_port_range_list:
            tcp_udp_parameters['source_port_range_list'] = source_port_range_list
        if destination_port_range_list:
            tcp_udp_parameters['destination_port_range_list'] = destination_port_range_list

        if tcp_udp_parameters:
            protocol_parameters[protocol.lower()] = tcp_udp_parameters

    elif protocol == 'ICMP':
        # Specifying ICMP code requires ICMP type to be specified as well
        if icmp_code and not icmp_type:
            print('ICMP Type must be specified as well if ICMP Code is specified.')
            exit(1)

        icmp_parameters = {}

        if icmp_type and icmp_type.upper() != 'ANY':
            icmp_parameters['icmp_type'] = int(icmp_type)

            if icmp_code and icmp_code.upper() != 'ANY':
                icmp_parameters['icmp_code'] = int(icmp_code)

        if icmp_parameters:
            protocol_parameters['icmp'] = icmp_parameters

    elif protocol == 'PROTOCOL_NUMBER':
        protocol_parameters['protocol_number'] = int(number_protocol)

    # Add details to base payload
    base_payload['spec']['resources']['protocol_type'] = protocol
    if protocol_parameters:
        base_payload['spec']['resources']['protocol_parameters'] = protocol_parameters
    return base_payload


# MAIN CODE

# Retrieve UUID of VPC tagged to tenant
vpc_filter = "category_name==TenantVisible;category_value=={}".format(TENANT_TAG)
response = ntnx_v3_api_post(pc_login, 'vpc', filter=vpc_filter)
print (str(response['metadata']['total_matches']))
if response['metadata']['total_matches'] != 1:
    print('Either no VPC or more than one VPC tagged to specified tenant.')
    exit(1)

vpc_details = response['entities'][0]
vpc_name = vpc_details['spec']['name']
vpc_uuid = vpc_details['metadata']['uuid']

# Consolidate list of all routes that are higher than fixed minimum priority
pbr_endpoint = '/api/nutanix/v3/routing_policies/list'  # Have to continue using this endpoint because it was already an established format with portal
pbr_payload = {
    'kind': 'routing_policy',
    'length': 999
}

pbr_list = ntnx_v3_api_post(pc_login, pbr_payload, api_extension=pbr_endpoint)

consolidated_pbr_list = []
for pbr in pbr_list['entities']:
    pbr_details = pbr['status']['resources']

    if pbr_details['vpc_reference']['uuid'] == vpc_uuid and pbr_details['priority'] >= int(minimum_priority):
        consolidated_pbr_list.append(pbr)

json_output = { 'entities': consolidated_pbr_list }
print(json.dumps(json_output))
