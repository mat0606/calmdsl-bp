user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"
payload = {
  "length": 250
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/accounts"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
account_list = []
account_list_json = r.json()
for account in account_list_json['entities']:
  if account['status']['name'] == "@@{account_name}@@": #sometimes this value will be '{}'
    print ("account_UUID=" + account['metadata']['uuid'])