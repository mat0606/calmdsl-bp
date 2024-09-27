user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"


  
payload = {
  "filter": "name==@@{Cluster_Name}@@",
  "kind": "cluster",
  "sort_order": "ASCENDING",
  "offset": 0,
  "length": 256,
  "sort_attribute": "name"
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/clusters"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
cluster_uuid = []
cluster_list_json = r.json()
for cluster in cluster_list_json['entities']:
  if cluster['spec']['name'] == "@@{Cluster_Name}@@": #sometimes this value will be '{}'
    print (cluster['metadata']['uuid'])
    exit(0)
exit(1)