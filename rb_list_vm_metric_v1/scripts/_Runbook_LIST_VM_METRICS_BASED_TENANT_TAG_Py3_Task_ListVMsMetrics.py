
# VARIABLE DECLARATION
TENANT_TAG = "@@{TENANT_TAG}@@"


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
def make_http_request(endpoint, method="GET", auth="BASIC", payload=None, username="", secret=""):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = urlreq(endpoint, verb=method, auth=auth, user=username, passwd=secret, params=payload, verify=False, headers=headers)
    print("REST elapsed total time: " + str(response.elapsed.total_seconds())) 

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

def pretty_print_json(json_dict):
    print(json.dumps(json_dict, ensure_ascii=False, indent=4))


# CUSTOM HELPER FUNCTIONS
def get_vm_metrics_details(prism_login, vm_uuid):
    vm_metrics_api = "/PrismGateway/services/rest/v1/vms/{}/stats/?metrics=hypervisor_cpu_usage_ppm,memory_usage_ppm,controller_user_bytes,disk_usage_ppm".format(vm_uuid)
    vm_metrics_details = ntnx_v3_api_get(prism_login, vm_metrics_api)
    return vm_metrics_details


# MAIN CODE
entity_filter = 'category_name==TenantVisible;category_value=={}'.format(TENANT_TAG)  
vm_details = ntnx_v3_api_post(pc_login, 'vm', filter=entity_filter)

vm_details_list = {}
for vm_detail in vm_details['entities']:
    vm_uuid = vm_detail['metadata']['uuid']
    vm_details_list[vm_uuid] = get_vm_metrics_details(pc_login, vm_uuid)

print(json.dumps(vm_details_list))
