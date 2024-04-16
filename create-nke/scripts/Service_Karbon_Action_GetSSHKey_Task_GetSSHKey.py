payload ={}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
pc_user = '@@{PC_Creds.username}@@'
pc_pass = '@@{PC_Creds.secret}@@'

# Set the address and make images call
#url = "https://localhost:9440/karbon/v1/k8s/clusters/@@{cluster_name}@@/kubeconfig"

url = "https://@@{PC_IP}@@:9440/karbon/v1/k8s/clusters/@@{cluster_name}@@/ssh"
resp = urlreq(url, verb='GET',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

if resp.ok:
  sshconfig = resp.json()
  print "certificate={}".format(sshconfig['certificate'])
  privateKeyPEM = sshconfig['private_key'].encode('utf8')
  print "private_key={}".format(privateKeyPEM)
  print "karbon_ssh={}".format(privateKeyPEM)
  print "username={}".format(sshconfig['username'])  
else:
  exit(1)
  

