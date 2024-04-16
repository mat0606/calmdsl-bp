user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"
payload = {
  "length": 250,
  "filter": "type==nutanix"
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/accounts"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
account_list = []
account_list_json = r.json()
print "Cluster Name: {}".format("@@{Cluster_Name}@@")
for account in account_list_json['entities']:
  data = account['status']['resources']['data']
  #print "json: {}".format(json.dumps(data))
  print "account name: {}".format(account['status']['name'])
  
  ## This section to replace the account name from PHX_POCxxx to PHX-POCxxx due to a bug in Calm VM 3.7.2.1 on PC2023.4
  clusterName = "@@{Cluster_Name}@@"
  accountName = account['status']['name']
  convertedAccountName = accountName.replace("_","-")
  print "account name after conversion: {}".format(convertedAccountName)
  ##
  
  if account['status']['resources']['type'] == 'azure' or account['status']['resources']['type'] == 'k8s' or account['status']['resources']['type'] =='aws' or account['status']['resources']['type'] == 'gcp':
#    print "resource type: {}",format(account['status']['resources']['type'])
    continue
  #elif data['host_pc'] == 'true':
#  elif account['status']['name'] == "@@{account_name}@@": #sometimes this value will be '{}'
  #elif accountName == clusterName:
  elif convertedAccountName == clusterName:
    #print "pe_account_UUID={}".format(data['cluster_account_reference_list'][0]['uuid'])
    print "pe_account_UUID={}".format(account['metadata']['uuid'])
    exit(0)

print "No PE Account UUID found"
exit(1)