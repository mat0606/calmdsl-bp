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
  print "Status code: {}".format(r.status_code)
  print "Output: {}".format(r.text)
  if r.ok:
    vpc_json = r.json()
      
    for vpc in vpc_json['entities']:
      if vpc['status']['state'] != 'COMPLETE':
        print "VPC {0} is in the midst of creation.  Sleeping for 10 seconds".format("@@{vpc_name}@@")
      elif vpc['status']['state'] == 'COMPLETE':
        print "vpc_uuid={0}".format(vpc['metadata']['uuid'])
        exit(0)
  elif r.status_code == 404:
    print "VPC {0} is in the midst of creation.  Sleeping for 10 seconds".format("@@{vpc_name}@@")
    
  count = count + 1
  sleep(10)    
print "No VPC {0} found after 60 seconds".format("@@{vpc_name}@@")
exit(1)
