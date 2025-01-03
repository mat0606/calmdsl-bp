user = "@@{CRED_PC.username}@@"
password = "@@{CRED_PC.secret}@@"
ip = "@@{PC_IP}@@"


payload = {
  
}

url = "https://" + ip + ":9440/api/vmm/v4.0/ahv/config/vms?$limit=100"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)

#print("REST elapsed total time: " + str(r.elapsed.total_seconds()))  
#print ("Output: " + r.text)
vm_list = []
if r.ok:
  vm_json = r.json()
  for vm in vm_json['data']:
    vm_list.append(vm['name'])
print (','.join(vm_list))    
