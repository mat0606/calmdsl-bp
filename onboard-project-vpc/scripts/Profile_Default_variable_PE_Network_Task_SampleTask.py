user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
def get_vpc_uuid(vpc_name):
  vpc_url = "https://"+ip+":9440/api/nutanix/v3/vpcs/list"
  params={
    "kind": "vpc"
  }
  r = urlreq(vpc_url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(params), verify=False, headers=headers)
  #print "status code: {}".format(r.status_code)
  #print "response: {}".format(r.text)
  vpc_list_json = r.json()
  #print "Before for loop"
  for vpc in vpc_list_json["entities"]:
   # print "In for loop"
    if vpc["spec"]["name"]==vpc_name:
   #   print "In VPC"
      return vpc["metadata"]["uuid"]
  print ("Unable to find a matching VPC: " + vpc_name)
  exit(1)

vpc_uuid=get_vpc_uuid("@@{vpc_name}@@")
#print "vpc_uuid: {}".format(vpc_uuid)


payload = {
  "kind": "subnet",
  "length": 500
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/subnets"
url = base_url + "/list"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
#print "Output: {}".format(r.text)
subnet_list = []
subnet_list_json = r.json()
for subnet in subnet_list_json['entities']:
#  print "{}".format(subnet['spec']['name'])
  if subnet['spec']['resources']['subnet_type'] == 'OVERLAY' and subnet['spec']['resources']['vpc_reference']['uuid'] == vpc_uuid:
    subnet_list.append("{}".format(subnet['spec']['name']))
print (','.join(subnet_list))