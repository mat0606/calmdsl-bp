user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

# filter by name because AOS 6.8 with PC2024.1 subnet list api failed without this name filter 
payload = {
  "filter": "name==VPC_External_Subnet"
  "kind": "subnet"
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/subnets"
url = base_url + "/list"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print ("Status code: " + str(r.status_code))
print ("Output: " + r.text)
subnet_list = []
subnet_list_json = r.json()
for subnet in subnet_list_json['entities']:
# print "cluster['spec']['name']"
  if subnet['spec']['resources']['subnet_type'] == 'VLAN':
    subnet_list.append(subnet['spec']['name'])
print (','.join(subnet_list))