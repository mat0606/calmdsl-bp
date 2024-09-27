user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
ip = "@@{CalmVM_IP}@@"

def process_request(url, method, user, password, headers, payload=None):
  r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
  return r

payload = {
  "kind": "marketplace_item",
  "sort_attribute": "name",
  "sort_order": "ASCENDING",
  "offset": 0,
  "length": 250
}

base_url = "https://" + ip + ":9440/api/nutanix/v3/calm_marketplace_items"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"

r = process_request(url, url_method, user, password, headers, json.dumps(payload))
#print "Response Status: " + str(r.status_code)
calm_marketplace_list_json = r.json()
#print calm_marketplace_list_json['metadata']['total_matches']
calm_marketplace_list = []
bp_uuid = ""
bp_name = ""
#count = 0
for calm_marketplace_item in calm_marketplace_list_json['entities']:
 # print calm_marketplace_item
 # count = count + 1
  #print count
  if calm_marketplace_item['status']['app_state'] == 'PUBLISHED' and bp_uuid != calm_marketplace_item['metadata']['uuid'] and bp_name != calm_marketplace_item['status']['name']: #sometimes this value will be '{
   # print "name: {} spec_version: {} version: {} uauid:{}".format(calm_marketplace_item['status']['name'], calm_marketplace_item['status']['spec_version'], calm_marketplace_item['status']['version'],calm_marketplace_item['metadata']['uuid'])
    calm_marketplace_list.append(calm_marketplace_item['status']['name'])
    bp_uuid = calm_marketplace_item['metadata']['uuid']
    bp_name = calm_marketplace_item['status']['name']

print (','.join(calm_marketplace_list))
