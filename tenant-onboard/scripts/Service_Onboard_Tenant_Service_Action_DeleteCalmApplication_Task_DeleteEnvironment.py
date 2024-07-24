
user = "@@{CalmVM Credential.username}@@" 
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"

def process_request(url, method, user, password, headers, payload=None):
  r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
  return r

payload = {
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/environments"
url = base_url + "/@@{Environment_UUID}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "DELETE"

r = process_request(url, url_method, user, password, headers, json.dumps(payload))

if r.ok:
  #json_resp = json.loads(r.content)
  print "Environment was deleted successfully"
else:
  print("Request failed")
  print("Headers: {}".format(headers))
  print('Status code: {}'.format(r.status_code))
  print('Response: {}'.format(json.dumps(json.loads(r.content), indent=4)))
  exit(1)
