
# VARIABLE DECLARATION

# set to True if CCF credentials are needed
CCF_CREDENTIALS_REQUIRED = False


# READ INPUT CREDENTIALS IF PROVIDED
try:
    input_credentials = json.loads('''@@{input_credentials}@@''')
except:
    input_credentials = {"ip_calm": "", "username_calm": "", "password_calm": "", "ip_pc": "", "username_pc": "", "password_pc": ""}

# Masked off by Matthew
#ip_calm, username_calm, password_calm = input_credentials.get('ip_calm', None), input_credentials.get('username_calm', None), input_credentials.get('password_calm', None)
#ip_pc, username_pc, password_pc = input_credentials.get('ip_pc', None), input_credentials.get('username_pc', None), input_credentials.get('password_pc', None)
#username_ccf, password_ccf = input_credentials.get('username_ccf', None), input_credentials.get('password_ccf', None)


# STANDARD HELPER FUNCTIONS
def make_http_request(endpoint, method="GET", auth="BASIC", payload=None, username="", secret=""):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = urlreq(endpoint, verb=method, auth=auth, user=username, passwd=secret, params=payload, verify=False, headers=headers)

    if not response.ok:
        print(response)
        print(response.json())

    response.raise_for_status()
    return response.json()

# Standard function to be used to call all Nutanix v3 GET APIs
def ntnx_v3_api_get(login_tuple, api_extension):
    username, secret = login_tuple[1], login_tuple[2]
    api_url = login_tuple[0] + api_extension

    response = make_http_request(api_url, username=username, secret=secret)
    return response

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

    response = make_http_request(api_url, method=req_method, payload=json.dumps(payload), username=username, secret=secret)
    return response

# Retrieves username and password from CyberArk CCP
def get_cyberark_secret(service_key):
    ccp_domains = {
        'i': 'ccp.tcloudsvc.gov.sg',
        'o': 'ccp.tcloudinf.gov.sg',
    }
    
    account_id = 'AIMWebService'
    app_id = 'Calm'
    
    service_vars_dict = {
        'calm': {
            'domain': ccp_domains['i'],
            'safe': 'clm_svc_lnx_da_itc',
            'object': 'clm_calm',
        },
        'pc': {
            'domain': ccp_domains['o'],
            'safe': 'npc_svc_lnx_da_otc',
            'object': 'npc_ten_calm',
        },
        'ccf': {
            'domain': ccp_domains['o'],
            'safe': 'ccf_svc_lnx_da_otc',
            'object': 'ccf_calm',
        },
    }
    
    service_vars = service_vars_dict[service_key]
    ccp_domain = service_vars['domain']
    safe_id = service_vars['safe']
    object_id = service_vars['object'].format(' ', '%20')

    ccp_api_url = "https://{}/{}/api/Accounts?AppID={}&Safe={}&Object={}".format(ccp_domain, account_id, app_id, safe_id, object_id)
    credentials = make_http_request(ccp_api_url, auth="No Auth")
    return credentials['UserName'], credentials['Content']

# CALM DETAILS - Masked off by Matthew
#if not ip_calm:
#    ip_calm = '10.55.88.50'

# Added by Matthew
ip_calm = '10.55.88.50'
print('ip_calm={}'.format(ip_calm))
# Masked off by Matthew because no CyberArk
#if not username_calm or not password_calm:
#    username_calm, password_calm = get_cyberark_secret('calm')

# Added by Matthew to bypass the CyberArk
username_calm = "@@{CRED_CALM.username}@@"
password_calm = "@@{CRED_CALM.secret}@@"
print('username_calm={}'.format(username_calm))
print('password_calm,secret={}'.format(password_calm))

calm_ip = "https://{}:9440".format(ip_calm)
calm_login = (calm_ip, username_calm, password_calm)


# PC DETAILS
# Added by Matthew
ip_pc = '' 
if not ip_pc:
    provider_details = ntnx_v3_api_post(calm_login, 'account')['entities']
    for entity in provider_details:
        if entity['status']['resources']['type'] == 'nutanix_pc' and entity['status']['name'] != 'NTNX_LOCAL_AZ':
            # Added by Matthew for Nutanix enviroment
        	if entity['status']['name'] == 'NTNX_LOCAL_AZ_ITC':
          		ip_pc = entity['status']['resources']['data']['server']
          		print ("PC_IP: " + ip_pc)

#print('ip_pc,secret={}'.format(ip_pc))
print('ip_pc={}'.format(ip_pc))

# Masked off by Matthew because we are not using Cyberark
#if not username_pc or not password_pc:
#    username_pc, password_pc = get_cyberark_secret('pc')

username_pc = "@@{CRED_PC.username}@@"
password_pc = "@@{CRED_PC.secret}@@"

print('username_pc={}'.format(username_pc))
print('password_pc,secret={}'.format(password_pc))

pc_ip = "https://{}:9440".format(ip_pc)
pc_login = (pc_ip, username_pc, password_pc)


# CCF CREDENTIALS
if CCF_CREDENTIALS_REQUIRED and (not username_ccf or not password_ccf):
    username_ccf, password_ccf = get_cyberark_secret('ccf')
    print('username_ccf={}'.format(username_ccf))
    print('password_ccf,secret={}'.format(password_ccf))