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
  #"sort_attribute": "user_name"
 
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/users"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)

#print "Response Status: " + str(r.status_code)
user_list_json = r.json()
print json.dumps(user_list_json)
user_list = []
users = "@@{Tenant_Consumer}@@"
selected_users = users.split(",")
print selected_users

def getUserJSON(user_name, user_uuid):
  user = {
    "kind": "user",
    "name": user_name,
    "uuid": user_uuid
  }
  return user
  
for user in user_list_json['entities']:
  if user['status']: #sometimes this value will be '{
    for selected_user in selected_users:
      if (user['status']['name'] == selected_user):
        #print "Tenant_Admin_UUID={}".format(user['metadata']['uuid'].encode('utf-8'))
        
        
        user_list.append(getUserJSON(user['status']['name'], user['metadata']['uuid']))
        print "Selected User: {} UUID: {}".format(user['status']['name'],user['metadata']['uuid'])
        break;

print "Tenant_Consumer_List={}".format(user_list)



