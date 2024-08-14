user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"


payload = {
  "filter": "name==@@{vpc_name}@@"
}

url = "https://" + ip + ":9440/api/nutanix/v3/vpcs/@@{vpc_uuid}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print ("Status code: " + r.status_code)
print ("Output: " + r.text)
if r.ok:
  print ("VPC @@{vpc_name}@@ is retrieved successfully")
else:
  exit(1)

vpc_route_table_uuid = "{}".format(str(uuid.uuid4()))
payload2 = {
  
  "spec": {
    "name": "Route Table for @@{vpc_name}@@",
    "resources": {
      "static_routes_list": [],
      "default_route_nexthop": {
        "external_subnet_reference": {
          "kind": "subnet",
          "name": "@@{PE_Network}@@",
          "uuid": "@@{pe_network_UUID}@@"
        }
      }
    }
  },
  "api_version": "3.1",
  "metadata": {
    "kind": "vpc_route_table",
    "uuid": vpc_route_table_uuid,
    "categories_mapping": {},
    "categories": {}
  }
}

url2 = "https://" + ip + ":9440/api/nutanix/v3/vpcs/@@{vpc_uuid}@@/route_tables"
headers2 = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method2 = "PUT"
r = urlreq(url2, url_method2, auth="BASIC", user=user, passwd=password, params=json.dumps(payload2), verify=False, headers=headers2)
#print ("Status code: " + r.status_code)
print ("Output: " + r.text)
if r.ok:
  print ("VPC @@{vpc_name}@@ static route is created successfully")
else:
  exit(1)
  
