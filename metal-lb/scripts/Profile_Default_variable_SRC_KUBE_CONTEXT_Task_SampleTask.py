payload ={}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
pc_user = '@@{PC Credential.username}@@'
pc_pass = '@@{PC Credential.secret}@@'

# Set the address and make images call
#url = "https://localhost:9440/karbon/v1-beta.1/k8s/clusters"
url = "https://@@{PC_IP}@@:9440/karbon/v1-beta.1/k8s/clusters"

r = urlreq(url, verb='GET',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)
#print("Status code: {}".format(r.status_code))
    
cluster_list_json = r.json()
cluster_list = []
# deal with the result/response
if r.ok:
  for cluster in cluster_list_json:
    if cluster['name']:
      cluster_list.append(cluster['name'])
else:
  print("Request failed")
  print("Headers: " + headers)
  print("Status code: " + r.status_code)
  print("Response: " + json.dumps(json.loads(r.content), indent=4))
  exit(1)
# endregion

print (",".join(cluster_list))