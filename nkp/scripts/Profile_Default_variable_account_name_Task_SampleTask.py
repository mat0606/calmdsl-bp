user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"
payload = {
  "filter": "type==@@{pc_calm_setup}@@"  
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/accounts"
#base_url = "https://10.55.49.50:9440/api/nutanix/v3/accounts"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
account_list = []
account_list_json = r.json()
for account in account_list_json['entities']:
  data = account['status']['resources']['data']
  if account['status']['name'] != 'NTNX_LOCAL_AZ':
    account_list.append(account['status']['name'])
print(','.join(account_list))
