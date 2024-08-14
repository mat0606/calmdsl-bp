  ## Create the Karbon Kubernetes cluster
  # Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {
}
      
pc_user = '@@{PC_Creds.username}@@'
pc_pass = '@@{PC_Creds.secret}@@'

  # Set the address and make images call
#url = "https://localhost:9440/karbon/v1/k8s/clusters/@@{cluster_name}@@"
url = "https://@@{PC_IP}@@:9440/karbon/v1/k8s/clusters/@@{cluster_name}@@"
resp = urlreq(url, verb='DELETE',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

  # If the call went through successfully, find the image by name
if resp.ok:
  print ("Cluster delete was successful" + json.dumps(json.loads(resp.content), indent=4))
  exit(0)

  # If the call failed
else:
  print ("Cluster delete failed" + json.dumps(json.loads(resp.content), indent=4))
  exit(1)

