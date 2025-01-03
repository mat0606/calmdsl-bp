
# STANDARD HELPER FUNCTIONS
def make_http_request(endpoint, method="GET", auth="BASIC", payload=None, username="", secret=""):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = urlreq(endpoint, verb=method, auth=auth, user=username, passwd=secret, params=payload, verify=False, headers=headers)

    if not response.ok:
        print(response.json())
        response.raise_for_status()

    return response.json()


# Standard function to be used to call all Nutanix v3 POST APIs
def ntnx_v3_api_post(login_tuple, payload, req_method="POST", api_extension=None, length=250, filter=None):
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

    return make_http_request(api_url, method=req_method, payload=json.dumps(payload), username=username, secret=secret)


# MAIN CODE

# Get Calm details
ip_calm = '@@{CalmVM_IP}@@'

username_calm = '@@{CRED_CALM.username}@@'
password_calm = '@@{CRED_CALM.secret}@@'

print('ip_calm={}'.format(ip_calm))
print('username_calm={}'.format(username_calm))
print('password_calm,secret={}'.format(password_calm))

calm_ip = "https://{}:9440".format(ip_calm)
calm_login = (calm_ip, username_calm, password_calm)

# Get PC details
provider_details = ntnx_v3_api_post(calm_login, 'account')['entities']
for entity in provider_details:
    if entity['status']['resources']['type'] == 'nutanix_pc' and entity['status']['name'] != 'NTNX_LOCAL_AZ':
      # Added by Matthew for Nutanix enviroment
      if entity['status']['name'] == '@@{account_name}@@':
        ip_pc = entity['status']['resources']['data']['server']
        print ("PC_IP: " + ip_pc)
        
calm_ip = "https://{}:9440".format(ip_calm)
calm_login = (calm_ip, username_calm, password_calm)

username_pc = '@@{CRED_PC.username}@@'
password_pc = '@@{CRED_PC.secret}@@'

#print('ip_pc,secret={}'.format(ip_pc))
print('ip_pc={}'.format(ip_pc))
print('username_pc={}'.format(username_pc))
print('password_pc,secret={}'.format(password_pc))
