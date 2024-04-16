user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"
payload = {
  "length": 250,
  "filter": "type==@@{pc_calm_setup}@@"  
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/accounts"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print r.text
#print r.json()
account_list = []
account_list_json = r.json()
for account in account_list_json['entities']:
#  cluster_uuid = account['status']['resources']['data']['cluster_uuid']
  data = account['status']['resources']['data']
  #print account
 # if 'cluster_uuid' in data:
    #if data['cluster_uuid'] == "@@{cluster_uuid}@@":
  account_list.append(account['status']['name'])
  #else:
  #  continue
    
print ",".join(account_list)
