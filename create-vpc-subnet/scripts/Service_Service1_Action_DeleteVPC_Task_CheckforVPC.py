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
      
    if vpc_json['metadata']['total_matches'] != 0:
      print "VPC: {} is in the midst of deletion.  Sleeping for 10 seconds".format("@@{vpc_name}@@")
    else:
      print "VPC: {} deleted successfully".format("@@{vpc_name}@@")
      exit(0)    
  count = count + 1
  sleep(10)    
print "VPC {0} was not deleted after 60 seconds.  Re-run this task if you think the VPC takes longer time than usual to delete".format("@@{vpc_name}@@")
exit(1)

