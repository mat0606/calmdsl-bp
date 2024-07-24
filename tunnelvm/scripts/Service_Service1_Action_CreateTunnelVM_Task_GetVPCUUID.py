user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

def get_vpc_uuid(vpc_name):
    vpc_url = "https://"+ip+":9440/api/nutanix/v3/vpcs/list"
    params={"kind": "vpc"}
    r = urlreq(vpc_url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(params), verify=False, headers=headers)
  #  print "status code: {}".format(r.status_code)
   # print "response: {}".format(r.text)
    vpc_list_json = r.json()
    for vpc in vpc_list_json["entities"]:
      if vpc["spec"]["name"]==vpc_name:
        return vpc["metadata"]["uuid"]
    exit(1)
vpc_uuid=get_vpc_uuid("@@{vpc_name}@@")
print "vpc_uuid={0}".format(vpc_uuid)
