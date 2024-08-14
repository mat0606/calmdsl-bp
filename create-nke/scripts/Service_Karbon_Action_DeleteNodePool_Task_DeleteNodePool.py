

  ## Create the Karbon Kubernetes cluster
  # Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {
  
}
  
pc_user = '@@{PC_Creds.username}@@'
pc_pass = '@@{PC_Creds.secret}@@'


  # Set the address and make images call
#url = "https://@@{PC_IP}@@:9440/karbon/v1-alpha.1/k8s/clusters/@@{cluster_name}@@/node-pools/@@{node_pool}@@"
# 9 Nov 23 - Encountered 404 error when using the v1-alpha.1 api
#url = "https://@@{PC_IP}@@:9440/karbon/v1-alpha.1/k8s/clusters/@@{cluster_name}@@/node-pools/@@{node_pool_name}@@"
url = "https://@@{PC_IP}@@:9440/karbon/v1-beta.1/k8s/clusters/@@{cluster_name}@@/node-pools/@@{node_pool_name}@@"

resp = urlreq(url, verb='DELETE',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

  # If the call went through successfully, find the image by name
if resp.ok:
  print ("Creation of task to remove Node Pool was successful" + json.dumps(json.loads(resp.content), indent=4))
  add_task_uuid = resp.json()['task_uuid']
  print ("task_uuid=" + add_task_uuid)
  exit(0)

  # If the call failed
else:
  print ("Creation of task to remove Node Pool failed" + json.dumps(json.loads(resp.content), indent=4))
  exit(1)

