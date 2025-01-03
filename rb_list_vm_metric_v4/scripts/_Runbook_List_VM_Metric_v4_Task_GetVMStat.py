
# VARIABLE DECLARATION
TENANT_TAG = "@@{tenant_tag}@@"
minimum_priority = "@@{minimum_priority}@@"

user = "@@{CRED_PC.username}@@"
password = "@@{CRED_PC.secret}@@"
ip = "@@{PC_IP}@@"

#print ("@@{vpc}@@")
payload = {
  "filter": "name==@@{vm}@@"
}

url = "https://" + ip + ":9440/api/vmm/v4.0/ahv/config/vms"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print ("Status code: " + r.status_code)
print("REST elapsed total time: " + str(r.elapsed.total_seconds()))  
print ("Output: " + r.text)
if r.ok:
  vm_json = r.json()
  vm = vm_json["data"][0]
  vmExtId = vm["extId"]
  print ("vmExtId: " + vmExtId)
  
url2 = "https://" + ip + ":9440/api/vmm/v4.0/ahv/stats/vms/" + vmExtId + "?$startTime=@@{startTime}@@&$statType=@@{statType}@@&$endTime=@@{endTime}@@&$samplingInterval=1&$select=@@{queryParam}@@"
#print (url2)
r2 = urlreq(url2, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print("REST elapsed total time: " + str(r2.elapsed.total_seconds()))  
print ("Output: " + r2.text)

 