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
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print "Status code: {}".format(r.status_code)
print "Output: {}".format(r.text)
if r.ok:
  vpc_json = r.json()
  for vpc in vpc_json['entities']:
    print "vpc_uuid={0}".format(vpc['metadata']['uuid'])
    exit(0)
print "No VPC {0} found".format("@@{vpc_name}@@")
exit(1)
