# Set creds and headers
era_user = '@@{era_server_creds.username}@@'
era_pass = '@@{era_server_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Cleanup the DB and get Operation ID
url = "https://@@{era_ip}@@:8443/era/v0.8/dbservers/@@{DB_SERVER_ID}@@?soft-remove=false&remove=false&delete=true&delete-vm-snapshots=true&delete-vgs=true"
resp = urlreq(url, verb='DELETE', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
print "DEREGISTER_OPERATION_ID={0}".format(json.loads(resp.content)['operationId'])