user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"


payload = {
  "kind": "vpc",
  "filter": "name==@@{vpc_name}@@"
}

url = "https://" + ip + ":9440/api/nutanix/v3/vpcs/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
count = 0
while count < 6:
  r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
  #print ("Status code: " + r.status_code)
  print ("Output: " + r.text)
  if r.ok:
    vpc_json = r.json()
      
    for vpc in vpc_json['entities']:
      if vpc['status']['state'] != 'COMPLETE':
        print ("VPC @@{vpc_name}@@ is in the midst of creation.  Sleeping for 10 seconds")
      elif vpc['status']['state'] == 'COMPLETE':
        print ("vpc_uuid=" + vpc['metadata']['uuid'])
        exit(0)
  elif r.status_code == 404:
    print ("VPC @@{vpc_name}@@ is in the midst of creation.  Sleeping for 10 seconds")
    
  count = count + 1
  sleep(10)    
print ("No VPC @@{vpc_name}@@ found after 60 seconds")
exit(1)
