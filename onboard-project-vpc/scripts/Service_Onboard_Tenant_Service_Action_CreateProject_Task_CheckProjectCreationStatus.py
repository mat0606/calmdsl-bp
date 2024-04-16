payload ={}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
pc_user = '@@{CalmVM Credential.username}@@'
pc_pass = '@@{CalmVM Credential.secret}@@'

ip = "@@{CalmVM_IP}@@"

payload = {
   "filter": "name==@@{Project_name}@@"  
}
count = 0
while(count < 5):
  # Set the address and make images call
  url = "https://" + ip + ":9440/api/nutanix/v3/projects/list"
  resp = urlreq(url, verb='POST',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

  # If the call went through successfully, find the image by name
  if resp.ok:
    project_json = resp.json()
    print project_json
    #if project_json['metadata']['length'] == 1:
    if project_json['metadata']['total_matches'] == 1:
      print "Project creation was successful", json.dumps(json.loads(resp.content), indent=4)
      exit(0)  
    else:
      print "Project Creation deployment not ready.  Sleeping for 60 seconds"
      count = count + 1
      sleep(60) #Sleep for 1 min
  # If the call failed
  else:
    print "Project creation failed", json.dumps(json.loads(resp.content), indent=4)
    exit(1)

print "Error: Operation Timeout after 5 mins"
exit(1)