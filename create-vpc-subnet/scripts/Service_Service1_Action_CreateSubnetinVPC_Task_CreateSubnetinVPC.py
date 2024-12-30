user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"


payload = {
  "spec": {
    "name": "@@{subnet_name}@@",
    "resources": {
      "subnet_type": "OVERLAY",
      "vpc_reference": {
        "kind": "vpc",
        "uuid": "@@{vpc_uuid}@@"
      },
      "external_connectivity_state": "ENABLED",
      "ip_config": {
        "pool_list": [
        {
          "range": "@@{Start_IP}@@ @@{End_IP}@@"
        }
        ],
        "subnet_ip": "@@{network_ip}@@",
        "prefix_length": @@{network_ip_prefix}@@,
        "default_gateway_ip": "@@{Gateway_IP}@@"
      }
    }
  },
  "metadata": {
    "kind": "subnet",
    "categories": {
      "@@{category}@@": "@@{category_value}@@"
    }
  }
}

url = "https://" + ip + ":9440/api/nutanix/v3/subnets"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print ("Status code: " + r.status_code)
print ("Output: " + r.text)
if r.ok:
  print ("Subnet @@{subnet_name}@@ in VPC @@{vpc_name}@@ is created successfully")
else:
  exit(1)