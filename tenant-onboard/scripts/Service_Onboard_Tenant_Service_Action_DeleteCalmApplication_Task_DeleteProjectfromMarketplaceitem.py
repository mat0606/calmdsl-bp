items = "@@{MarketPlace_item}@@"
selected_marketplace_items = items.split(",")
print selected_marketplace_items

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
selected_marketplace_items_uuid = []
bp_uuid = ""
bp_name = ""
for calm_marketplace_item in calm_marketplace_list_json['entities']:
  for selected_mp_item in selected_marketplace_items:
    if calm_marketplace_item['status']['name'] == selected_mp_item and bp_uuid != calm_marketplace_item['metadata']['uuid'] and bp_name != calm_marketplace_item['status']['name']: #sometimes this value will be '{
      print "name: {} uuid: {}".format(calm_marketplace_item['status']['name'], calm_marketplace_item['metadata']['uuid'])
      selected_marketplace_items_uuid.append(calm_marketplace_item['metadata']['uuid'])
      bp_uuid = calm_marketplace_item['metadata']['uuid']
      bp_name = calm_marketplace_item['status']['name']
                                             
print selected_marketplace_items_uuid         

url_method = "GET"
payload2 = {}
project_spec = {
    "kind": "Project",
    "name": "@@{Project_name}@@",
    "uuid": "@@{Project_UUID}@@"
  }

for mp_item_uuid in selected_marketplace_items_uuid:
  
  url2 = base_url + "/" + mp_item_uuid
  r2 = process_request(url2, url_method, user, password, headers, json.dumps(payload2))
  mp_item_json = r2.json()
  mp_item_json.pop("status", None)
  
  project_ref_array = mp_item_json['spec']['resources']['project_reference_list']
  count = 0
  for project in project_ref_array:
    if project['name'] == "@@{Project_name}@@":
      project_ref_array.pop(count)
      count = count + 1
     # mp_item_json['spec']['resources']['project_reference_list'] = project_ref_array
      url3_method = "PUT"
      r3 = process_request(url2, url3_method, user, password, headers, json.dumps(mp_item_json))
      if r3.ok:
        print "Removing project: {} from marketplace item uuid: {}".format("@@{Project_name}@@", mp_item_uuid)
        print mp_item_json['spec']['resources']['project_reference_list']
      else:
        print "Unable to remove project {} from marketplace item uuid: {}".format("@@{Project_name}@@", mp_item_uuid)
        print "Status Code: {} Response: {}".format(r3.status_code, r3.text)
      break
    else:
      continue
  