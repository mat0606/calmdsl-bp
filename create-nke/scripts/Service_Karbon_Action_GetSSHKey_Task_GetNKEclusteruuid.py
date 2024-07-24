payload ={}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
pc_user = '@@{PC_Creds.username}@@'
pc_pass = '@@{PC_Creds.secret}@@'

# Set the address and make images call
url = "https://@@{PC_IP}@@:9440/karbon/v1/k8s/clusters/@@{cluster_name}@@"
resp = urlreq(url, verb='GET',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)
#resp = requests.post(url, json=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

if resp.ok:
  cluster_config = resp.json()
  print ("nke_cluster_uuid=" + cluster_config['uuid'])
else:
  print ("Failure to retrieve nke cluster information")
