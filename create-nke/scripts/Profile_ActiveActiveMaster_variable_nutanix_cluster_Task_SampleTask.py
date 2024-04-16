user = "@@{PC_Creds.username}@@"
password = "@@{PC_Creds.secret}@@"
ip = "@@{PC_IP}@@"

def getClusterIP(pc_ip, cluster_uuid, pc_user, pc_password):
  payload = {}
  base_cluster_url = "https://" + pc_ip + ":9440/api/nutanix/v3/clusters"
  cluster_url = base_cluster_url + "/" + cluster_uuid
  cluster_url_method = "GET"
  r2 = urlreq(cluster_url, cluster_url_method, auth="BASIC", user=pc_user, passwd=pc_password, params=json.dumps(payload), verify=False, headers=headers)
  #print r.json()
  cluster_uuid = []
  cluster_list_json = r2.json()
  return cluster_list_json['spec']['resources']['network']['external_ip']
#########################################################################################

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
    if cluster['spec']['name'].encode('utf-8') != 'Unnamed':
    #if cluster['spec']['name'] != 'Unnamed':
      clusterIP = getClusterIP(ip, cluster['metadata']['uuid'],user,password)
      #print clusterIP
      cluster_list.append(cluster['spec']['name'])
  print ",".join(cluster_list)      
else: 
  exit(1)