user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "DELETE"

network_group_tunnel_uuid = "{}".format(str(uuid.uuid4()))
tunnel_uuid = "{}".format(str(uuid.uuid4()))

payload = {
}  

#base_url = "https://" + ip + ":9440/api/nutanix/v3/tunnels/@@{tunnel_uuid}@@"
base_url = "https://" + ip + ":9440/api/nutanix/v3/network_groups/@@{network_group_uuid}@@/tunnels/@@{tunnel_uuid}@@"
url = base_url
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print "Status code: {}".format(r.status_code)
print "Output: {}".format(r.text)
if r.ok:
  print "Successful deletion of tunnel VM"
else:
  exit(1)