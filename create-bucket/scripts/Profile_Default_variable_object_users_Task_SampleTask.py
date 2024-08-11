user = "@@{PC_Creds.username}@@"
password = "@@{PC_Creds.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
 
}

base_url = "https://" + ip + ":9440/oss/iam_proxy/users"
url = base_url
#print url
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)

if r.ok:
  user_list_json = r.json()
  user_list = []
  for user in user_list_json['users']:
    user_list.append(user['username'])
  print (','.join(user_list))    
else:
  print ("Response Status: " + str(r.status_code))
  print (r.text)
