user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

payload = {
  "kind": "subnet"
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/subnets"
url = base_url + "/list"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
#print "Output: {}".format(r.text)
subnet_list = []
subnet_list_json = r.json()
for subnet in subnet_list_json['entities']:
# print "cluster['spec']['name']"
  if subnet['spec']['resources']['subnet_type'] == 'VLAN':
    subnet_list.append("{}".format(subnet['spec']['name']))
print ','.join(subnet_list)