user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"
pe_user = "@@{PE Credential.username}@@"
pe_password = "@@{PE Credential.secret}@@"

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

def getMemoryUtilization(pe_ip, pe_user, pe_password):
  payload = {}
  pe_base_url = "https://" + pe_ip + ":9440/PrismGateway/services/rest/v2.0/cluster/stats"
  pe_url = pe_base_url + "/?metrics=hypervisor_memory_usage_ppm&interval_in_sec=60"
  headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
  pe_url_method = "GET"
  
  #print "Memory Utilization: Before REST service"
  r3 = urlreq(pe_url, pe_url_method, auth="BASIC", user=pe_user, passwd=pe_password, params=json.dumps(payload), verify=False, headers=headers)
  #print r3.text
  if r3.ok: 
    cluster_list_json = r3.json()
    #print cluster_list_json
    memory_ppm = float(cluster_list_json['stats_specific_responses'][0]['values'][0])
   # print "memory_ppm: {}".format(memory_ppm)
    memory_ppm = memory_ppm / 10000
    return memory_ppm
  else:
    print ("Error in retrieving Prism Element Memory Statistics: Status Code: " + str(r3.status_code) + " Response: " + r3.text)
    exit(1)
    

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
  memoryUtilization = 100
  for cluster in cluster_list_json['entities']:
    #print cluster['spec']['name']
    if cluster['spec']['name'].encode('utf-8') != 'Unnamed':
    #if cluster['spec']['name'] != 'Unnamed':
      clusterIP = getClusterIP(ip, cluster['metadata']['uuid'],user,password)
      #print clusterIP
      memoryUtilization = getMemoryUtilization(clusterIP, pe_user, pe_password)
     # print "Cluster IP: {} Memory Utilization: {}".format(clusterIP, memoryUtilization)
      cluster_list.append({
        "cluster_name": cluster['spec']['name'], 
        "cluster_memory": memoryUtilization
      })

  #print "Bubble-sort the lowest memory utilization"
  lowest_memory_utilization = 100
  lowest_memory_cluster = ""
  for cluster in cluster_list:
    if cluster['cluster_memory'] < lowest_memory_utilization:
      lowest_memory_utilization = cluster['cluster_memory']
      lowest_memory_cluster = cluster['cluster_name']

  #print "lowest_memory_cluster: {}  lowest_memory_utilization: {}".format(lowest_memory_cluster, lowest_memory_utilization)
  if lowest_memory_cluster != '':
    print (lowest_memory_cluster)
  else:
    exit(1)
else: 
  exit(1)