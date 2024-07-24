import base64

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
  print ("certificate=" + sshconfig['certificate'])
  #privateKeyPEM = sshconfig['private_key'].encode('utf8')
  # https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
  privateKeyByte = sshconfig['private_key'].encode('ascii')
  private_key_base64_bytes = base64.b64encode(privateKeyByte)
  private_key_base64_decode_str = private_key_base64_bytes.decode('ascii')
  
  # Encode to base64 because ----- OPENSSH ------ will cause the 1st line to be passed and not the other line
  print ("private_key=" + private_key_base64_decode_str)
  print ("karbon_ssh=" + private_key_base64_decode_str)
  print ("username={}" + sshconfig['username'])  
  print ("original_private_key=" + sshconfig['private_key'])
else:
  exit(1)
  

