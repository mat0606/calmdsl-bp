user = "@@{CalmVM Credential.username}@@" 
password = "@@{CalmVM Credential.secret}@@"
#ip = "@@{PC_IP}@@"
ip = "@@{CalmVM_IP}@@"

payload = {
   "filter": "name==Consumer",
    "kind": "role",
    "offset": 0,
    "length": 50,
    "sort_order": "ASCENDING",
    "sort_attribute": "name" 
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/roles"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)

if r.ok:
  role_list_json = r.json()
  if role_list_json['metadata']['total_matches'] == 1:
    print "consumer_role_UUID={}".format(role_list_json['entities'][0]['metadata']['uuid'])
  else:
    print "There is more than 1 Consumer role.  Please contact your system administrator to check the configuration"
    exit(1)
else:
  print "Status Code: {} Response: {}".format(r.status_code, r.text)
  exit(1)


