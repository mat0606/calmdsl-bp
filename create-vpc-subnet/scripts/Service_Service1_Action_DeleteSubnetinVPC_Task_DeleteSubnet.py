user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
 
}

url = "https://" + ip + ":9440/api/nutanix/v3/subnets/@@{subnet_uuid}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "DELETE"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print ("Status code: " + r.status_code)
#print "Output: {}".format(r.text)
if r.ok:
  print ("Subnet @@{subnet_name}@@ is deleted successfully")
else:
  exit(1)