## Get Karbon Image UUID
# Set the headers, payload, and cookies
#user = "@@{PC_Creds.username}@@" 
#password = "@@{PC_Creds.secret}@@"
user = "@@{CalmVM_Cred.username}@@"
password = "@@{CalmVM_Cred.secret}@@"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = {
 "filter": "name==@@{calm_project_name}@@"
}


# Set the address and make projects call
#url = "https://localhost:9440/api/nutanix/v3/projects/list"
url = "https://@@{CalmVM_IP}@@:9440/api/nutanix/v3/projects/list"

resp = urlreq(url, verb='POST', params=json.dumps(payload), headers=headers, verify=False, auth="BASIC", user=user, passwd=password)

# If the call went through successfully, find the project by name
if resp.ok:
  for entity in json.loads(resp.content)['entities']:
    if entity['status']['name'] == '@@{calm_project_name}@@':
      # if CalmVM_IP is in the same PC
      if "@@{CalmVM_IP}@@" == "@@{PC_IP}@@":
        for subnet in entity['status']['resources']['subnet_reference_list']:
          if subnet['name'] == '@@{network_name}@@':
            print "SUBNET_UUID={0}".format(subnet['uuid'])
            exit(0)
        else:
          print "Network '@@{network_name}@@' is not available in project '@@{calm_project_name}@@'.  Please check the network name and try again."
          exit(1)
      else: #CalmVM is in different PC
        # This approach may retrieve the wrong subnet uuid under the following conditions:
        #  1.  Calm VM has multiple account provider with the same subnet name.  Eg cluster 218 with primary subnet and cluster 170 with primary subnet
        #  Workaround:
        #    Change the name of the subnet from primary to primary_218 for cluster 218 and from primary to primary_170 to cluster_170
        for subnet in entity['spec']['resources']['external_network_list']:
          if subnet['name'] == '@@{network_name}@@':
            print "SUBNET_UUID={0}".format(subnet['uuid'])
            exit(0)
        else:
          print "Network '@@{network_name}@@' is not available in project '@@{calm_project_name}@@'.  Please check the network name and try again."
          exit(1)
        
# If the call failed
else:
  print "Projects call failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)

# If we made it this far, there was an error
print "ERROR: '@@{calm_project_name}@@' project was not found."
exit(0)