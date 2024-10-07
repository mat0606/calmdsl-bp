user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
  "kind": "cluster",
  "sort_attribute": "name",
  "sort_order": "ASCENDING"
  
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/clusters"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
#print "Output: {}".format(r.text)
if r.ok:
  cluster_list = []
  cluster_list_json = r.json()
  #print cluster_list_json
  for cluster in cluster_list_json['entities']:
    #print cluster['spec']['name']
    if cluster['spec']['name'] != 'Unnamed':
      cluster_list.append(cluster['spec']['name'])
else: 
  exit(1)
print (','.join(cluster_list))