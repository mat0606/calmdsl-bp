user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
 
}

url = "https://" + ip + ":9440/api/networking/v4.0/config/subnets/@@{subnet_uuid}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print ("Status code: " + str(r.status_code))
print ("Output: " + r.text)
r_header = r.headers
print ("ETag: " + r_header['Etag'])
if r.ok:
  url_method2 = "DELETE"
  header2 = {'Accept': 'application/json', 'Content-Type': 'application/json', 'NTNX-Request-Id': str(uuid.uuid4())}
  r2 = urlreq(url, url_method2, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=header2)
  print ("Status code: " + str(r2.status_code))
  print ("Output: " + r2.text)
  if r2.ok:
    taskId = r2.json()['data']['extId']
    print ("Task Id" + taskId + " created to delete Subnet @@{subnet_name}@@")
    print ("taskId==" + taskId)
    exit(0)
  else:
    exit(1)    
else:
  exit(1)