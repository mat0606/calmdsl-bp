# Set creds and headers
era_user = '@@{era_server_creds.username}@@'
era_pass = '@@{era_server_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Get Cluster ID
url     = "https://@@{era_ip}@@:8443/era/v0.8/clusters"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
print "Status Code: {}".format(resp.status_code)
print "Response: {}".format(resp.text)
if resp.ok:
  print "CLUSTER_ID={0}".format(json.loads(resp.content)[0]['id'])
else:
  exit(1)