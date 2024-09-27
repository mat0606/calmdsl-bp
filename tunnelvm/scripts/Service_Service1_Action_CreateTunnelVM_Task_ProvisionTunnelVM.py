user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

network_group_tunnel_uuid = "{}".format(str(uuid.uuid4()))
tunnel_uuid = "{}".format(str(uuid.uuid4()))

payload = {
  "api_version": "3.1.0",
  "metadata": {
    "kind": "network_group_tunnel",
    "uuid": network_group_tunnel_uuid
  },
  "spec": {
    "resources": {
      "platform_vpc_uuid_list": [
        "@@{vpc_uuid}@@"
      ],
      "tunnel_reference": {
        "kind": "tunnel",
        "uuid": tunnel_uuid,
        "name": "NTNX_LOCAL_AZ_VPC_@@{vpc_name}@@_Tunnel"
      },
      "account_reference": {
        "kind": "account",
        "name": "@@{account_name}@@",
        "uuid": "@@{account_UUID}@@"
      },
      "tunnel_vm_spec": {
        "vm_name": "@@{vpc_name}@@_@@{subnet_name}@@_TunnelVM",
        "subnet_uuid": "@@{pe_network_UUID}@@",
        "cluster_uuid": "@@{pe_cluster_uuid}@@"
      }
    },
    "name": "VPC_@@{vpc_name}@@_NTNX_LOCAL_AZ"
  }
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/network_groups/tunnels"
url = base_url
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
print ("Output: " + r.text)
if r.ok:
  print ("Successful invocation of tunnel VM")
  print ("network_group_uuid=" + network_group_tunnel_uuid)
else:
  exit(1)