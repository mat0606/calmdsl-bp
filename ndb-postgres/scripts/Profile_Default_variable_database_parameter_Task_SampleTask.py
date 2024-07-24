headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
era_user = '@@{era_server_creds.username}@@'
era_pass = '@@{era_server_creds.secret}@@'
#era_ip = '10.38.197.125'
era_ip = '@@{era_ip}@@'

# Get Compute Profile ID
url     = "https://" + era_ip + ":8443/era/v0.8/profiles?type=Database_Parameter"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
#print "NETWORK_PROF_ID={0}".format(json.loads(resp.content)['id'])
a = ''
for i in resp.json():
  a = a + i['name'] + ','
print re.sub(',$', '', a)