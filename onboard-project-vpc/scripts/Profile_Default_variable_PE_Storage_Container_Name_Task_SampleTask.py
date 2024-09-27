user = "@@{PE Credential.username}@@"
pe_password = "@@{PE Credential.secret}@@"

# Sleep for 10 seconds for retrieval of cluster ip
sleep(10)

payload = {
  "length": 250
  
}

ip = "@@{cluster_ip}@@"
  
#print "PE IP: {}".format(ip)
base_url = "https://" + ip + ":9440/PrismGateway/services/rest/v2.0/storage_containers"
url = base_url 
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=pe_password, params=json.dumps(payload), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
#print "Output: {}".format(r.text)
sc_list = []
sc_list_json = r.json()
for sc in sc_list_json['entities']:
 # print "cluster['spec']['name']"
  sc_list.append("{}".format(sc['name']))
  
if len(sc_list) > 0:  
  print (','.join(sc_list))
else:
  exit(1)