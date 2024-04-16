user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
  "filter": "name==@@{vpc_name}@@"
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/vpcs"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
#print "Output: {}".format(r.text)
vpc_list = []
vpc_list_json = r.json()
for vpc in vpc_list_json['entities']:
  if vpc['spec']['name'] == "@@{vpc_name}@@":
    print vpc['spec']['name']
    print "vpc_uuid={0}".format(vpc['metadata']['uuid'])
    exit(0)
print "No VPC {0} found".format("@@{vpc_name}@@")
exit(1)  

