payload ={}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
pc_user = '@@{CalmVM Credential.username}@@'
pc_pass = '@@{CalmVM Credential.secret}@@'

ip = "@@{CalmVM_IP}@@"

count = 0
while(count < 10):
  # Set the address and make images call
  #url = "https://localhost:9440/karbon/v1/k8s/clusters/@@{cluster_name}@@/health"
  url = "https://" + ip + ":9440/api/nutanix/v3/network_groups/@@{network_group_uuid}@@/verify"
  resp = urlreq(url, verb='GET',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

  # If the call went through successfully, find the image by name
  if resp.ok:
    print "Tunnel creation was successful", json.dumps(json.loads(resp.content), indent=4)
    exit(0)
  
  elif (resp.status_code == 412):
    print "Tunnel VM deployment not ready.  Sleeping for 60 seconds"
    count = count + 1
    sleep(60) #Sleep for 1 min
  # If the call failed
  else:
    print "Tunnel VM failed", json.dumps(json.loads(resp.content), indent=4)
    exit(1)

print "Error: Operation Timeout after 10 mins"
exit(1)