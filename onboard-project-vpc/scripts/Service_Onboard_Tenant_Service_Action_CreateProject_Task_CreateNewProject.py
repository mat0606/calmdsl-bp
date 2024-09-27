user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
#ip = "@@{PC_IP}@@"
ip = "@@{CalmVM_IP}@@"

consumer_list = @@{Tenant_Consumer_List}@@
user_reference_list = @@{Tenant_Admin_List}@@
for consumer in consumer_list:
  user_reference_list.append(consumer)
  
selected_project_admin_list = @@{Tenant_Admin_List}@@
# Choose the 1st project admin user to be the owner reference list
selected_owner = selected_project_admin_list.pop()
print ("selected_owner: " + selected_owner)

env_reference_list = [
                    {
                        "kind": "environment",
                        "uuid": "@@{Environment_UUID}@@"
                    }
                ]
                
if "@@{CalmVM_IP}@@" == "@@{PC_IP}@@":
  
  payload = {
    "spec": {
      "description": "Project for @@{Project_name}@@",
      "resources": {
        "cluster_reference_list": [
          {
            "kind": "cluster",
            "uuid": "@@{cluster_uuid}@@"
          }
        ],
        "account_reference_list": [
          {
            "kind": "account",
            "uuid": "@@{account_UUID}@@"
       #  "uuid": "@@{pe_account_UUID}@@"
         
          }
        ],
        "vpc_reference_list": [
          {
            "kind": "vpc",
            "name": "@@{vpc_name}@@",
            "uuid": "@@{vpc_uuid}@@"
          }
        ],
        "subnet_reference_list": [
          {
            "kind": "subnet",
            "name": "@@{PE_Network}@@",
            "uuid": "@@{pe_network_UUID}@@"
          }
        ],
        "resource_domain": {
          "resources": []
        },
        "user_reference_list": user_reference_list,
    #  "environment_reference_list": env_reference_list,
        "external_network_list": []
      },
      "name": "@@{Project_name}@@"
    },
    "metadata": {
      "kind": "project",
      "name": "@@{Project_name}@@",
      "owner_reference": selected_owner
    },
    "api_version": "3.1"
  }

    
else:
 
  payload = {
    "spec": {
      "description": "Project for @@{Project_name}@@",
      "resources": {
        "cluster_reference_list": [
          {
            "kind": "cluster",
            "uuid": "@@{cluster_uuid}@@"
          }
        ],
        "account_reference_list": [
          {
            "kind": "account",
            "uuid": "@@{account_UUID}@@"
       #  "uuid": "@@{pe_account_UUID}@@"
         
          }
        ],
        "vpc_reference_list": [
          {  
             "kind": "vpc",
             "name": "@@{vpc_name}@@",
             "uuid": "@@{vpc_uuid}@@"
          }
        ],
     #   "resource_domain": {
     #     "resources": []
     #   },
        "user_reference_list": user_reference_list,
        "external_network_list": [
          {
            "name": "@@{PE_Network}@@",
            "uuid": "@@{pe_network_UUID}@@"
          }
        ]
      },
      "name": "@@{Project_name}@@"
    },
    "metadata": {
      "kind": "project",
      "name": "@@{Project_name}@@",
      "owner_reference": selected_owner
    },
    "api_version": "3.1"
  }

print (payload)
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
  
url2 = "https://" + ip + ":9440/api/nutanix/v3/projects"
url_method = "POST"
r2 = urlreq(url2, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Response Status: {}".format(r2.status_code)
print ("Response: ", r2.json())
if r2.ok:
  project2_json = r2.json()
  project_uuid = project2_json['metadata']['uuid']
  print (json.dumps(project2_json))
  print ("Project_UUID=" + project_uuid))
else:
  print ("Status code: " + str(r2.status_code) + " Response: " + r2.text)
  exit(1)