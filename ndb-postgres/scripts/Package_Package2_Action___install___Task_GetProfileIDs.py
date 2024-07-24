# Set creds and headers
era_user = '@@{era_server_creds.username}@@'
era_pass = '@@{era_server_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Get Software Profile ID
url     = "https://@@{era_ip}@@:8443/era/v0.8/profiles?type=Software&name=@@{software_profile}@@"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
print "Status Code: {}".format(resp.status_code)
if resp.ok:
  print "SOFTWARE_PROF_ID={0}".format(json.loads(resp.content)['id'])
else:
  exit(1)

# Get Compute Profile ID
url     = "https://@@{era_ip}@@:8443/era/v0.8/profiles?type=Compute&name=@@{compute_profile}@@"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
print "Status Code: {}".format(resp.status_code)
if resp.ok:
  print "COMPUTE_PROF_ID={0}".format(json.loads(resp.content)['id'])
else:
  exit(1)

# Get Compute Profile ID
url     = "https://@@{era_ip}@@:8443/era/v0.8/profiles?type=Network&name=@@{network_profile}@@"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
print "Status Code: {}".format(resp.status_code)
if resp.ok:
  print "NETWORK_PROF_ID={0}".format(json.loads(resp.content)['id'])
else:
  exit(1)

# Get Compute Profile ID
url     = "https://@@{era_ip}@@:8443/era/v0.8/profiles?type=Database_Parameter&name=@@{database_parameter}@@"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
print "Status Code: {}".format(resp.status_code)
if resp.ok:
  print "DB_PARAM_ID={0}".format(json.loads(resp.content)['id'])
else:
  exit(1)