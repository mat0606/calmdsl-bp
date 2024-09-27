user = "@@{PE Credential.username}@@" 
password = "@@{PE Credential.secret}@@"
ip = "@@{PE_IP}@@"

def process_request(url, method, user, password, headers, payload=None):
  r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
  return r
payload = {}
base_url = "https://" + ip + ":9440/PrismGateway/services/rest/v2.0/cluster"
url = base_url + "/"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"

r = process_request(url, url_method, user, password, headers, json.dumps(payload))

cluster_list = []
cluster_list_json = r.json()

print ("pe_cluster_uuid=" + cluster_list_json['uuid'])


