# Set creds and headers
era_user = '@@{era_server_creds.username}@@'
era_pass = '@@{era_server_creds.secret}@@'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# Get DB Server IP and ID
url     = "https://@@{era_ip}@@:8443/era/v0.8/databases/name/@@{DB_ENTITY_NAME}@@?detailed=true"
resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)

if resp.ok:
  print "DB_SERVER_IP={0}".format(json.loads(resp.content)['hostIP'])
  print "DB_ID={0}".format(json.loads(resp.content)['id'])
  print "DB_SERVER_ID={0}".format(json.loads(resp.content)['primaryHost'])
  # Get DB Server Name
  url     = "https://@@{era_ip}@@:8443/era/v0.8/dbservers/" + json.loads(resp.content)['primaryHost']
  resp = urlreq(url, verb='GET', auth='BASIC', user=era_user, passwd=era_pass, headers=headers)
  if resp.ok:
    print "DB_SERVER_NAME={0}".format(json.loads(resp.content)['name'])

    prop = json.loads(resp.content)['properties']
    for i in prop:
      if i["name"] == "vm_cluster_uuid":
        print "DB_SERVER_VM_UUID={0}".format(i["value"])
  else:
    print "Error executing api to retrieve database server {0} Response: {1}".format(resp.status_code, resp.text)  

else:
  print "Error executing api to retrieve database information: {0} Response: {1}".format(resp.status_code, resp.text)  

