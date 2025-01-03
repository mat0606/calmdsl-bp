
# VARIABLE DECLARATION
TENANT_TAG = "@@{tenant_tag}@@"
minimum_priority = "@@{minimum_priority}@@"

user = "@@{CRED_PC.username}@@"
password = "@@{CRED_PC.secret}@@"
ip = "@@{ip_pc}@@"

#print ("@@{vpc}@@")
payload = {
  "filter": "name==@@{vpc}@@"
}

url = "https://" + ip + ":9440/api/networking/v4.0/config/routing-policies"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print ("Status code: " + r.status_code)
print("REST elapsed total time: " + str(r.elapsed.total_seconds()))  
print ("Output: " + r.text)
pbr_list = []
if r.ok:
  pbr_json = r.json()
  for pbr in pbr_json['data']:
    pbr_list.append(pbr['name'])
print (','.join(pbr_list))    
