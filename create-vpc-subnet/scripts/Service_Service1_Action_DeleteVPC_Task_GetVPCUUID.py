user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
#  "filter": "name==@@{vpc_name}@@"
}

#base_url = "https://" + ip + ":9440/api/nutanix/v3/vpcs"
#url = base_url + "/list"
url = "https://" + ip + ":9440/api/networking/v4.0/config/vpcs?$filter=name eq '@@{vpc_name}@@'"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
#print "Output: {}".format(r.text)
vpc_list = []
vpc_list_json = r.json()
for vpc in vpc_list_json['data']:
  if vpc['name'] == "@@{vpc_name}@@":
    print (vpc['name'])
    print ("vpc_uuid=" + vpc['extId'])
    exit(0)
print ("No VPC @@{vpc_name}@@ found")
exit(1)  

