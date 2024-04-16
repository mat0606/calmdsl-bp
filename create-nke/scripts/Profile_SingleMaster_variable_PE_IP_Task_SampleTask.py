user = "@@{PC_Creds.username}@@"
password = "@@{PC_Creds.secret}@@"
ip = "@@{PC_IP}@@"
payload = {
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/clusters"
url = base_url + "/@@{nutanix_cluster_uuid}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print r.json()
cluster_uuid = []
cluster_list_json = r.json()
print cluster_list_json['spec']['resources']['network']['external_ip']