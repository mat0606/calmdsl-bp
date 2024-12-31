user = "@@{CRED_PC.username}@@"
password = "@@{CRED_PC.secret}@@"
ip = "10.42.155.39"


payload = {
  
}

url = "https://" + ip + ":9440/api/networking/v4.0/config/vpcs"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print ("Status code: " + r.status_code)
#print ("Output: " + r.text)
vpc_list = []
if r.ok:
  vpc_json = r.json()
  for vpc in vpc_json['data']:
    vpc_list.append(vpc['name'])
print (','.join(vpc_list))    
