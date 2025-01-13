user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
}

#base_url = "https://" + ip + ":9440/api/nutanix/v3/subnets"
#url = base_url + "/list"
url = "https://" + ip + ":9440/api/networking/v4.0/config/subnets?$filter=vpcReference eq '@@{vpc_uuid}@@'"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print ("Status code: " + str(r.status_code))
print ("Output: " + r.text)
subnet_list = []
subnet_list_json = r.json()
for subnet in subnet_list_json['data']:
  if subnet['name'] == "@@{subnet_name}@@":
    print (subnet['name'])
    print ("subnet_uuid=" + subnet['extId'])
    exit(0)
print ("No Subnet @@{subnet_name}@@ found")
exit(1)  

