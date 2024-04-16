user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"


payload = {
  "spec": {
    "name": "@@{vpc_name}@@",
    "resources": {
      "common_domain_name_server_ip_list": [
      {
        "ip": "@@{dns}@@"
      }
      ],
      "external_subnet_list": [
      {
        "external_subnet_reference": {
          "kind": "subnet",
          "uuid": "@@{pe_network_UUID}@@"
        }
      }
      ] #,
     # "externally_routable_prefix_list": [
     # {
       # "ip": "@@{ext_routable_ip}@@",
       # "prefix_length": @@{ext_routable_ip_prefix}@@
     # }
     # ]
    }
  },
#  "description": "on prem VPC",
  "api_version": "3.0",
  "metadata": {
    "kind": "vpc",
    "categories": {
      "VirtualNetworkType": "Tenant"
    }
  }
}

url = "https://" + ip + ":9440/api/nutanix/v3/vpcs"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print "Status code: {}".format(r.status_code)
print "Output: {}".format(r.text)
if r.ok:
  print "VPC {0} is in the midst of creation".format("@@{vpc_name}@@")
else:
  exit(1)
