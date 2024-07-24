user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{pc_ip}@@"
uuid = "@@{DB_SERVER_VM_UUID}@@"

print "local UUID" + uuid

def process_request(url, method, user, password, headers, payload=None):
  r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
  return r

payload = {"length":500}

base_url = "https://" + ip + ":9440/api/nutanix/v3/vms"
url = base_url + "/" + uuid
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"

r = process_request(url, url_method, user, password, headers, json.dumps(payload))
print "Response Status: " + str(r.status_code)
vm_json = r.json()

del vm_json['status']
vm_json['metadata']['categories'] = {}

print "Categories: " + json.dumps(vm_json['metadata']['categories'])
print "VM JSON: " + json.dumps(vm_json)

url = base_url + "/" + str(vm_json['metadata']['uuid'])
url_method = "PUT"
r = process_request(url, url_method, user, password, headers, json.dumps(vm_json))
print "Response Status: " + str(r.status_code)
print "Response: ", r.json()
