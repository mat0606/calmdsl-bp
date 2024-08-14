

  ## Create the Karbon Kubernetes cluster
  # Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {
 
}
  
pc_user = '@@{PC_Creds.username}@@'
pc_pass = '@@{PC_Creds.secret}@@'


  # Set the address and make images call
url = "https://localhost:9440/karbon/v1-alpha.1/k8s/clusters/@@{cluster_name}@@/node-pools"
resp = urlreq(url, verb='GET',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

pool_list = []
  # If the call went through successfully, find the image by name
if resp.ok:
  pool_list_json = resp.json()
 # print pool_list_json
  for pool in pool_list_json:
    # print "cluster['spec']['name']"
    if pool['name'] == 'worker-node-pool' or pool['name'] == 'master-node-pool' or pool['name'] == 'etcd-node-pool':
      continue
    else:
      pool_list.append(pool['name'])
  
#print ','.join(pool_list)    
print (",".join(pool_list))    

