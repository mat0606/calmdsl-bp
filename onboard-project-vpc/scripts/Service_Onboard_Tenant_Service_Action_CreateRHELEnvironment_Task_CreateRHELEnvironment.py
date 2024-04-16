
selected_project_admin_list = @@{Tenant_Admin_List}@@
# Choose the 1st project admin user to be the owner reference list
selected_owner = selected_project_admin_list.pop()
print "selected_owner: {}".format(selected_owner)


env_name = "ENV{}".format(str(uuid.uuid4()))
user = "@@{CalmVM Credential.username}@@" 
password = "@@{CalmVM Credential.secret}@@"
#ip = "@@{PC_IP}@@"
ip = "@@{CalmVM_IP}@@"

ip_str = "@"+"@" + "{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}"+ "@"+"@"


infra_list = [
  {
    "cluster_references": [{
      "uuid": "@@{cluster_uuid}@@"
    }],
    "default_subnet_reference": {
      "uuid": "@@{pe_network_UUID}@@"
    },
    "account_reference": {
      "kind": "account",
      "name": "@@{account_name}@@",
      "uuid": "@@{account_UUID}@@"
      #"uuid": "@@{pe_account_UUID}@@"
    },
    "vpc_references": [
    {
      "uuid": "@@{vpc_uuid}@@"
    }],
    "subnet_references": [
    {
      "uuid": "@@{pe_network_UUID}@@"
    }],
    "type": "nutanix_pc"
    
  }
]




WIN_SPEC = @@{WIN_SPEC}@@
LINUX_SPEC = @@{LINUX_SPEC}@@
substrate_list = []
substrate_list.append(WIN_SPEC)
substrate_list.append(LINUX_SPEC)

ENV_SPEC = {
    "spec": {
        "name": env_name,
        "resources": {
          "infra_inclusion_list": infra_list,
          "substrate_definition_list": substrate_list,
          "credential_definition_list": @@{credential_list}@@
        }
    },
    "api_version": "3.1.0",
    "metadata": {
        "kind": "environment",
        "owner_reference": selected_owner,
        "name": env_name,
        "project_reference": {
          "kind": "project",
          "name": "@@{Project_name}@@",
          "uuid": "@@{Project_UUID}@@" 
        }
    }
}

print "Environment: {}".format(json.dumps(ENV_SPEC))
base_url = "https://" + ip + ":9440/api/nutanix/v3/environments"
url = base_url 
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(ENV_SPEC), verify=False, headers=headers)

if r.ok:
  json_resp = json.loads(r.content)
  print "Environment_UUID={}".format(json_resp["metadata"]["uuid"])
else:
  print("Request failed")
  print("Headers: {}".format(headers))
  print('Status code: {}'.format(r.status_code))
  print('Response: {}'.format(json.dumps(json.loads(r.content), indent=4)))
  exit(1)

