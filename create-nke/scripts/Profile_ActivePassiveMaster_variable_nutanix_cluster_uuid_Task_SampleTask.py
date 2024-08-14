
user = "@@{PC_Creds.username}@@"
password = "@@{PC_Creds.secret}@@"

ip = "@@{PC_IP}@@"

def process_request(url, method, user, password, headers, payload=None):
  r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
  return r
payload = {}
#base_url = "https://" + ip + ":9440/PrismGateway/services/rest/v2.0/cluster"
base_url = "https://" + ip + ":9440/api/clustermgmt/v4.0.a1/config/clusters"

url = base_url + "/"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"

r = process_request(url, url_method, user, password, headers, json.dumps(payload))

cluster_list = []
cluster_list_json = r.json()

#print "PE_Cluster_UUID={}".format(cluster_list_json['uuid'])
for cluster in cluster_list_json['data']:
  if cluster['name'] == "@@{nutanix_cluster}@@":
    #print "{}".format(cluster['extId'])
    print ("".join(cluster['extId'])) 
    exit(0)
print ("No cluster uuid found")
exit(1)

