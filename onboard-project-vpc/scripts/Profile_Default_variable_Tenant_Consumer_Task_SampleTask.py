user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"

def process_request(url, method, user, password, headers, payload=None):
  r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
  return r

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
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

r = process_request(url, url_method, user, password, headers, json.dumps(payload))
#print "Response Status: " + str(r.status_code)
user_list_json = r.json()
user_list = []
for user in user_list_json['entities']:
  if user['status']: #sometimes this value will be '{
    user_list.append(user['status']['name'].encode('utf-8'))

print (','.join(user_list))    
