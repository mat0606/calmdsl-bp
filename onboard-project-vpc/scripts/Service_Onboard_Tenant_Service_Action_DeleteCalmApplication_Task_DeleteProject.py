user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"


payload = {
  "uuid": "@@{Project_UUID}@@",
}


base_url = "https://" + ip + ":9440/api/nutanix/v3/projects"
url = base_url + "/@@{Project_UUID}@@"
url_method = "DELETE"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print r.status_code
