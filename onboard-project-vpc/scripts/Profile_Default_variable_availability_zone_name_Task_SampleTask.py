user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"

payload = {
  "length": 50
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/availability_zones"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print r.status_code
#print r.text
az_list = []
az_list_json = r.json()
for az in az_list_json['entities']:
  az_list.append(az['spec']['name'])
print (",".join(az_list))