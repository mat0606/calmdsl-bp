user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

payload = {
  "kind": "tunnel",
  "filter": "name==NTNX_LOCAL_AZ_VPC_@@{vpc_name}@@_Tunnel"
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/tunnels/list"
url = base_url
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print "Status code: {}".format(r.status_code)
print "Output: {}".format(r.text)
if r.ok:
  print "Successful retrieval of tunnel VM"
  tunnel_json = r.json()
  for tunnel in tunnel_json['entities']:
    if tunnel['metadata']['name'] == 'NTNX_LOCAL_AZ_VPC_@@{vpc_name}@@_Tunnel':
      print "tunnel_uuid={}".format(tunnel['metadata']['uuid'])
      exit(0)
else:
  exit(1)