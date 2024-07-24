# Set creds, headers, and payload
user = '@@{PC_Creds.username}@@'
password = '@@{PC_Creds.secret}@@'
ip = "@@{PC_IP}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

user_list = []
users = "@@{object_users}@@"
selected_users = users.split(",")
print selected_users

def getUserJSON(user_name):
  user = {
    "username": user_name,
    "permissions": [
        "READ",
        "WRITE"
      ]
  }
  return user
  
for selected_user in selected_users:
    user_list.append(getUserJSON(selected_user))
    print "Selected User: {}".format(selected_user)
  

payload = {
  "name": "@@{bucket_name}@@",
  "bucket_permissions": user_list
}


print payload
# Set the url and make the call
url = "https://" + ip + ":9440/oss/api/nutanix/v3/objectstores/@@{object_store_uuid}@@/buckets/@@{bucket_name}@@/share"
resp = urlreq(url, verb='PUT', auth='BASIC', user=user, passwd=password, params=json.dumps(payload), headers=headers, verify=False)

# If the call went through successfully
if resp.ok:
  print("User @@{object_users}@@ added to bucket '@@{bucket_name}@@' successfully.")

# If the call failed
else:
  print(url + " call failed.")
  print(resp)
  exit(1)