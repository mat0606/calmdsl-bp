user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"
payload = {
  "length": 250,
  "filter": "type==nutanix_pc"  
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
if r.ok:
  for account in account_list_json['entities']:
#  cluster_uuid = account['status']['resources']['data']['cluster_uuid']
    if account['metadata']['name'] == "@@{account_name}@@":
      data = account['status']['resources']['data']
  #print account
      if 'cluster_account_reference_list' in data:
        for cluster_account in data['cluster_account_reference_list']:
          print "cluster_account_reference_UUID={}".format(cluster_account['uuid'])
          exit(0)
else:
  print "Status Code: {0} Response: {1}".format(r.status_code, r.text)
  
print "Unable to find cluster account reference uuid"
exit(1)
 