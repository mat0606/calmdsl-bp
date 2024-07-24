user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
#ip = "@@{PC_IP}@@"
ip = "@@{CalmVM_IP}@@"

payload = {
  # Mask off the payload due to https://jira.nutanix.com/browse/CALM-32740
  #"kind": "user",
  #"sort_order": "ASCENDING",
  #"offset": 0,
  #"length": 256,
  #"sort_attribute": "name"
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/users"
url = base_url + "/list"
#print url
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)

if r.ok:
  user_list_json = r.json()
  user_list = []
  for user in user_list_json['entities']:
    if user['status']: #sometimes this value will be '{
      user_list.append(user['status']['name'].encode('utf-8'))
  print ','.join(user_list)    
else:
  print "Response Status: " + str(r.status_code)
  print r.text
