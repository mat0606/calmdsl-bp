start_time_test = _datetime.datetime.now()
# VARIABLE DECLARATION
TENANT_UUID = "@@{tenant_uuid}@@"
ip_pc = "@@{PC_IP}@@"

# AUTHENTICATION
username_calm = "@@{CRED_CALM.username}@@"
password_calm = "@@{CRED_CALM.secret}@@"
calm_ip = "https://{}:9440".format("@@{CalmVM_IP}@@")
calm_login = (calm_ip, username_calm, password_calm)

username_pc = "@@{CRED_PC.username}@@"
password_pc = "@@{CRED_PC.secret}@@"
pc_ip = "https://{}:9440".format(ip_pc)
pc_login = (pc_ip, username_pc, password_pc)

# STANDARD HELPER FUNCTIONS
def make_http_request(endpoint, method="GET", payload=None, auth="BASIC", username="", secret="", add_headers={}, silence_errors=False, max_attempts=50, sleep_seconds=15, nutx_session_token=None):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    for key, value in add_headers.items():
        headers[key] = value

    while max_attempts > 0:
        response = urlreq(endpoint, verb=method, params=payload, headers=headers, verify=False, auth=auth, user=username, passwd=secret)
        print ("Response Elapsed Time:" + str(response.elapsed.total_seconds()))  
        print ("Response Text: " + response.text)
    
        if response.ok:
            break
        else:
            if response.status_code in [408, 409, 422] or response.status_code >= 500:
                # 409 means conflict in request, could sometimes refer to concurrent requests for Nutanix
                # 422 means hit requests threshold, can retry after delay
                # 500 error codes are server errors, worth retrying
                max_attempts -= 1
                if max_attempts > 0:
                    sleep(sleep_seconds)
                    continue

            if not silence_errors:
                print(response.json())
                response.raise_for_status()

    try:   # try to return a JSON object, else return text
        return response.json()
    except:
        return response.text


# Standard function to get a proxy token for a specified Nutanix user
def get_nutx_proxy_token(login_tuple, proxy_username):
    username, secret = login_tuple[1], login_tuple[2]
    proxy_url = login_tuple[0] + '/api/nutanix/v3/proxy_login'

    payload = { "proxy_for_username": proxy_username }
    response = make_http_request(proxy_url, method='POST', payload=json.dumps(payload), username=username, secret=secret)

    token = response['ntnx_igw_session']
    headers = {
        "Cookie": "NTNX_IGW_SESSION={}".format(token)
    }
    return headers

# Standard function to be used to call all GET APIs
def ntnx_v4_api_get(login_tuple, api_extension, proxy_username=None, silence_errors=False):
    username, secret = login_tuple[1], login_tuple[2]

    if api_extension[0] != '/':
        api_extension = '/{}'.format(api_extension)
    api_url = login_tuple[0] + api_extension

    if proxy_username:
        headers = get_nutx_proxy_token(login_tuple, proxy_username)
        return make_http_request(api_url, auth="", add_headers=headers, silence_errors=silence_errors)
    else:
        return make_http_request(api_url, username=username, secret=secret, silence_errors=silence_errors)
        
# Standard function to be used to call all Nutanix v3 POST APIs
def ntnx_v4_api_post(login_tuple, payload, req_method="POST", api_extension=None, length=None, filter=None, proxy_username=None, silence_errors=False):
    username, secret = login_tuple[1], login_tuple[2]

    # convert to standard list entity URL if no override provided
    if api_extension:
        if api_extension[0] != '/':
            api_extension = '/{}'.format(api_extension)
        api_url = login_tuple[0] + api_extension

    # insert optional length into payload
    if length:
        api_url = '{}?$limit={}'.format(api_url, length)
        
    # insert optional filter into payload
    if length and filter:
        api_url = '{}&{}'.format(api_url, filter)
    
    if not length and filter:
        api_url = '{}?{}'.format(api_url, filter)

    # if payload is empty, ensure it is an empty dictionary
    if not payload:
        payload = {}

    if proxy_username:
        headers = get_nutx_proxy_token(login_tuple, proxy_username)
        return make_http_request(api_url, method=req_method, payload=json.dumps(payload), auth="", add_headers=headers, silence_errors=silence_errors)
    else:
        return make_http_request(api_url, method=req_method, payload=json.dumps(payload), username=username, secret=secret, silence_errors=silence_errors)

def pretty_print_json(json_dict):
    print(json.dumps(json_dict, ensure_ascii=False, indent=4))


# CUSTOM HELPER FUNCTIONS
# def get_vm_uuid(prism_login):
#     vm_uuid_api = "/api/vmm/v4.0/ahv/config/vms/?$limit=100&$select=categories,extId"
#     vm_uuid = ntnx_v4_api_get(prism_login, vm_uuid_api)
#     return vm_uuid

def get_vm_metrics_details(prism_login, vm_uuid_list, start_time, end_time, sampling_interval=3600*9):
    stats_list = "stats/diskUsagePpm,stats/memoryUsagePpm,stats/numVcpusUsedPpm"
    vm_metrics_dict = {}
    vm_metrics_url = "/api/vmm/v4.0/ahv/stats/vms"
    vm_metrics_filter = "$startTime={}&$endTime={}&$samplingInterval={}&$select={}&$statType=LAST".format(start_time, end_time, sampling_interval, stats_list)
    # print(vm_metrics_url)
    vm_metrics_details = compile(vm_metrics_url,vm_metrics_filter)
    # print(vm_metrics_details)
    for extId in vm_metrics_details["data"]:
        vm_metrics_key = extId["extId"]
        if vm_metrics_key in vm_uuid_list:
            vm_metrics_value = extId["stats"][-1]
            vm_metrics_dict[vm_metrics_key] = vm_metrics_value
    return vm_metrics_dict

def compile(api_ext, api_filter=None, length=100):
    compiled_response = []
    compiling = True
    compiled_length = 0
    page = 0
    while compiling:
        filter="$page={}".format(page)
        if api_filter:
            filter = "{}&{}".format(api_filter,filter)
        response = ntnx_v4_api_post(pc_login, None, req_method="GET", api_extension=api_ext, length=length, filter=filter)
        compiled_length = compiled_length + len(response["data"])
        if compiled_response:
            compiled_response["data"].extend(response["data"])
        else:
            compiled_response = response
        if compiled_length == response["metadata"]["totalAvailableResults"]:
            compiling = False
        page += 1
    return compiled_response

# MAIN CODE
counter = 50
vm_uuid_api = "/api/vmm/v4.0/ahv/config/vms"
filter="$select=categories,extId"
# response = compile(vm_uuid_api, )
response = compile(vm_uuid_api, filter, )

# print(json.dumps(response))
# data_list = response["data"]

# vm_uuid_list = []
# for data in data_list:
#     category_uuid_list = data.get("categories", None)
#     if category_uuid_list is not None:
#         for category in category_uuid_list:
#             if category["extId"] == TENANT_UUID:
#                 vm_uuid = data["extId"]
#                 vm_uuid_list.append(vm_uuid)
#     # if len(vm_uuid_list) == counter:
#     #     break

# print(len(vm_uuid_list))
# # print(json.dumps(response))
# vm_list_time = _datetime.datetime.now()
# time_format = "%Y-%m-%dT%H:%M:%SZ"
# end_time = _datetime.datetime.now()
# fmt_end_time = end_time.strftime(time_format)

# time_diff = _datetime.timedelta(hours=9)
# start_time = end_time - time_diff
# fmt_start_time = start_time.strftime(time_format)
# print(fmt_start_time)
# print(fmt_end_time)

# vm_metrics_details_response = get_vm_metrics_details(prism_login=pc_login,vm_uuid_list=vm_uuid_list,start_time=fmt_start_time,end_time=fmt_end_time)
# print(len(vm_metrics_details_response))
# vm_metrics_details_list = json.dumps(vm_metrics_details_response)
# print(len(vm_metrics_details_list))

end_time_test = _datetime.datetime.now()
print(start_time_test)
#print(vm_list_time)
print(end_time_test)