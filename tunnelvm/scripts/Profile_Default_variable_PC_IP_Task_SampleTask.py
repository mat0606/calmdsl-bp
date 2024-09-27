user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"
payload = {
  "length": 250,
  "filter": "name==@@{account_name}@@"  
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/accounts"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print r.text
#print r.json()
account_list_json = r.json()
for account in account_list_json['entities']:
  data = account['status']['resources']['data']
  print (data['server'])
  exit(0)
  

