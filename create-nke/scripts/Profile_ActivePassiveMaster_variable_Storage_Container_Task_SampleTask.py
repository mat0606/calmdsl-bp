user = "@@{PC_Creds.username}@@"
password = "@@{PC_Creds.secret}@@"
#ip = "@@{PE_IP}@@"
ip = "@@{PC_IP}@@"
payload = {
  
}
 
#print "PE IP: {}".format(ip)
#base_url = "https://" + ip + ":9440/PrismGateway/services/rest/v2.0/storage_containers"
#base_url = "https://" + ip + ":9440/api/storage/v4.0.a2/config/storage-containers"
# changed by Matthew because the previous v4 api does not work for PC2024.1 and NKE 2.10
base_url = "https://" + ip + ":9440/api/clustermgmt/v4.0.b2/config/storage-containers"
url = base_url 
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
#print "Output: {}".format(r.text)
sc_list = []
sc_list_json = r.json()
#for sc in sc_list_json['entities']:
 # print "cluster['spec']['name']"
#  sc_list.append("{}".format(sc['name']))
for sc in sc_list_json['data']:
  if sc['clusterExtId'] == "@@{nutanix_cluster_uuid}@@":
    sc_list.append(sc['name'])
  
#print ','.join(sc_list)    
print (",".join(sc_list))     
