user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"
payload = {}
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
  vpc_list.append("{}".format(vpc['spec']['name']))
print (','.join(vpc_list))