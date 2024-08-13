# Set creds, headers, and payload
user = '@@{PC_Creds.username}@@'
password = '@@{PC_Creds.secret}@@'
ip = "@@{PC_IP}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

user_list = []
users = "@@{object_users}@@"
selected_users = users.split(",")
print (selected_users)

def getUserJSON(user_name, sid):
  user = {
    "Action": "s3:*",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::bucket",
      "Principal": {
        "AWS": [
          user_name
        ]
      },
      "Resource": "arn:aws:s3:::bucket",
      "Sid": sid
  }
  return user
  
for selected_user in selected_users:
    # hardcode the sid for adminisrator now.  Need time to retrieve the owner statement
    user_list.append(getUserJSON(selected_user,"Owner_Statement_1723538721825"))
    print ("Selected User: " + selected_user)

print (user_list)
  
payload = {
  "Statement": user_list,
  "Version": "2.0"
}
print (payload)
# Set the url and make the call
url = "https://" + ip + ":9440/oss/api/nutanix/v3/objectstore_proxy/@@{object_store_uuid}@@/buckets/@@{bucket_name}@@/policy"
# Masked off temporary.
#resp = urlreq(url, verb='PUT', auth='BASIC', user=user, passwd=password, params=json.dumps(payload), headers=headers, verify=False)

# If the call went through successfully
#if resp.ok:
#  print("User @@{object_users}@@ added to bucket '@@{bucket_name}@@' successfully.")
#else:
#  print(url + " call failed.")
#  print(resp.text)
#  exit(1)