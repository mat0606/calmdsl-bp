

  ## Create the Karbon Kubernetes cluster
  # Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {
  "ahv_config": {
    "cpu": @@{node_cpu}@@, #required
    "disk_mib": @@{node_disk_mib}@@, #required
  #  "iscsi_network_name": "string",
  #  "iscsi_network_uuid": "string",
    "memory_mib": @@{node_memory_mib}@@, #required
  #  "network_name": "string",
  #  "network_uuid": "string",
  #  "prism_element_cluster_uuid": "string"
  },
 # "gpu_config_list": [
 #   {
 #     "count": 1,
 #     "name": "@@{gpu_model}@@" #required
 #   }
 # ],
 # "labels": {
 #   "property1": "string",
 #   "property2": "string"
 # },
  "name": "@@{node_pool_name}@@", #required
  "node_os_version": "@@{image_name}@@",
  "num_instances": @@{num_nodes}@@
}
  
pc_user = '@@{PC_Creds.username}@@'
pc_pass = '@@{PC_Creds.secret}@@'


  # Set the address and make images call
  
#url = "https://localhost:9440/karbon/v1-alpha.1/k8s/clusters/@@{cluster_name}@@/add-node-pool"
url = "https://@@{PC_IP}@@:9440/karbon/v1-alpha.1/k8s/clusters/@@{cluster_name}@@/add-node-pool"
resp = urlreq(url, verb='POST',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

  # If the call went through successfully, find the image by name
if resp.ok:
  print ("Creation of task to create Worker Node Pool was successful" + json.dumps(json.loads(resp.content), indent=4))
  add_task_uuid = resp.json()['task_uuid']
  print ("task_uuid=" + add_task_uuid)
  exit(0)

  # If the call failed
else:
  print ("Creation of task to create Worker Node Pool failed" + json.dumps(json.loads(resp.content), indent=4))
  exit(1)

