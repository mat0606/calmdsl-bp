user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
  
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/subnets"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print "Status code: {}".format(r.status_code)
print "Output: {}".format(r.text)
if r.ok:
  subnet_list = []
  subnet_list_json = r.json()
  for subnet in subnet_list_json['entities']:
 # print "cluster['spec']['name']"
#  print subnet
    if subnet['spec']['name'] == "@@{external_subnet}@@":
      print "pe_network_UUID={}".format(subnet['metadata']['uuid'])
      exit(0)
  print "Unable to find pe network"   
  exit(1)
else:
  exit(1)