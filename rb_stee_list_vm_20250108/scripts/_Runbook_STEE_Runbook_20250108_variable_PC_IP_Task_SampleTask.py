user = "@@{CRED_CALM.username}@@"
password = "@@{CRED_CALM.secret}@@"
ip = "@@{CalmVM_IP}@@"
payload = {
  "length": 10,
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
  if account['status']['resources']['type'] == 'nutanix_pc' and account['status']['name'] != 'NTNX_LOCAL_AZ':
      # Added by Matthew for Nutanix enviroment
      if account['status']['name'] == '@@{account_name}@@':
        ip_pc = account['status']['resources']['data']['server']
        print (ip_pc)
  

