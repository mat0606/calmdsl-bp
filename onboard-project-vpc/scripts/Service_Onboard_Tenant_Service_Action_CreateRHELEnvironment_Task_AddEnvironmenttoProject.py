user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
#ip = "@@{PC_IP}@@"
ip = "@@{CalmVM_IP}@@"


 
base_url = "https://" + ip + ":9440/api/nutanix/v3/projects_internal"
url = base_url + "/@@{Project_UUID}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, verify=False, headers=headers)
print ("Status Code: " + str(r.status_code))
print ("Response: " + r.text)
if r.ok:
  project_json = r.json()
  project_json.pop("status", None)
  # associate the environment to the project
  project_json['spec']['project_detail']["resources"]["environment_reference_list"] = [
    {
      "kind": "environment",
      "uuid": "@@{Environment_UUID}@@"
    }
  ]

  project_json['spec']['project_detail']['resources']['vpc_reference_list'] = [
    { 
      "kind": "vpc",
      "uuid": "@@{vpc_uuid}@@"
    }
  ]
  project_json['spec']['project_detail']['resources']['external_network_list'] = [
    {
      "name": "@@{PE_Network}@@",
      "uuid": "@@{pe_network_UUID}@@"
    }
  ]
else:
  print ("Error retrieving project")
  exit(1)
print ("Project JSON to put: " + project_json)
base_url = "https://" + ip + ":9440/api/nutanix/v3/projects_internal"
url = base_url + "/@@{Project_UUID}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "PUT"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(project_json), verify=False, headers=headers)
print ("Status code: " + str(r.status_code))
print ("Response: " + r.text)
if r.ok:
  print ("Successful addition of environment uuid: @@{Environment_UUID}@@ ")
else:
  print ("Unable to add environment uuid @@{Environment_UUID}@@ to project")
  exit(1)
