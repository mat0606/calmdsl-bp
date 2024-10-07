user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
  "kind": "subnet",
  "sort_attribute": "name",
  "sort_order": "ASCENDING"
  
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/subnets"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
#print "Output: {}".format(r.text)
if r.ok:
  subnet_list = []
  subnet_list_json = r.json()
  #print cluster_list_json
  for subnet in subnet_list_json['entities']:
    subnet_list.append(subnet['spec']['name'])
else: 
  exit(1)
print (','.join(subnet_list))