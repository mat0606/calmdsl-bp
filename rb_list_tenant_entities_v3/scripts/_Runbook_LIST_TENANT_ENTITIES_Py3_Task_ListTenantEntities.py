
# VARIABLE DECLARATION
tenant_tag = '@@{tenant_tag}@@'
ENTITY_TYPE = '@@{ENTITY_TYPE}@@'.lower()


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


# MAIN CODE
entity_filter = 'category_name==TenantVisible;category_value=={}'.format(tenant_tag)
entity_details = ntnx_v3_api_post(pc_login, ENTITY_TYPE, filter=entity_filter)
print(json.dumps(entity_details))