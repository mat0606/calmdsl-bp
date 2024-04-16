user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"


payload = {
  "filter": "name==@@{subnet_name}@@"
}

url = "https://" + ip + ":9440/api/nutanix/v3/subnets/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
count = 0
while count < 6:
  r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
  print "Status code: {}".format(r.status_code)
  print "Output: {}".format(r.text)
  if r.ok:
    subnet_json = r.json()
    for subnet in subnet_json['entities']:
      if subnet['spec']['resources']['subnet_type'] == 'OVERLAY':
        if subnet['status']['state'] != 'COMPLETE':
          print "Subnet {0} is in the midst of creation.  Sleeping for 10 seconds".format("@@{subnet_name}@@")
          count = count + 1
          sleep(10)
        elif subnet['status']['state'] == 'COMPLETE':
          print "subnet_uuid={0}".format(subnet['metadata']['uuid'])
          exit(0)
  elif r.status_code == 404:
    print "Subnet {0} is in the midst of creation.  Sleeping for 10 seconds".format("@@{subnet_name}@@")
    count = count + 1
    sleep(10)

print "No Subnet {0} found after 60 seconds".format("@@{subnet_name}@@")
exit(1)
