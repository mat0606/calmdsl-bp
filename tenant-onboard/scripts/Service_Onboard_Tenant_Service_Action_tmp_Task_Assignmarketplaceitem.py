#script
items = "Centos 7 in VPC,RHEL85 VM in VPC,Windows 2019"
selected_marketplace_items = items.split(",")
print selected_marketplace_items

user = "matthew.ong@infra.demo.local"
password = "xxxxxxxxxx"
ip = "172.16.101.10"

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

if r.ok:
#print "Response Status: " + str(r.status_code)
  calm_marketplace_list_json = r.json()
  selected_marketplace_items_uuid = []
  bp_uuid = ""
  bp_name = ""
  for calm_marketplace_item in calm_marketplace_list_json['entities']:
    for selected_mp_item in selected_marketplace_items:
      print "current mpi name: {0} current_selected_mp_item {1}".format(calm_marketplace_item['status']['name'], selected_mp_item)
      print "bp_uuid: {0} current mpi uuid: {1}".format(bp_uuid, calm_marketplace_item['metadata']['uuid'])
      print "bp_name: {0} current mpi name: {1}".format(bp_name, calm_marketplace_item['status']['name'])
      print "current mpi json: {}".format(calm_marketplace_item)
      if calm_marketplace_item['status']['name'] == selected_mp_item and bp_uuid != calm_marketplace_item['metadata']['uuid'] and bp_name != calm_marketplace_item['status']['name']: #sometimes this value will be '{
        print "name: {} uuid: {}".format(calm_marketplace_item['status']['name'], calm_marketplace_item['metadata']['uuid'])
        selected_marketplace_items_uuid.append(calm_marketplace_item['metadata']['uuid'])
        bp_uuid = calm_marketplace_item['metadata']['uuid']
        bp_name = calm_marketplace_item['status']['name']
else:
  print "Unable to list Marketplace Items"
  print "Status Code: {} Response: {}".format(r.status_code, r.text)
  exit(1)
  
print "selected mpi uuid: {}".format(selected_marketplace_items_uuid)

url_method = "GET"
payload2 = {}
project_spec = {
    "kind": "project",
    "name": "tenant05",
    "uuid": "a5b7b031-2dd9-4d7c-92f3-28372d0c983c"
  }

print "Adding project spec to mp: {}".format(project_spec)
for mp_item_uuid in selected_marketplace_items_uuid:
  
  url3 = base_url + "/" + mp_item_uuid
  r2 = process_request(url3, url_method, user, password, headers, json.dumps(payload2))
  if r2.ok:
    mp_item_json = r2.json()
    mp_item_json.pop("status", None) 
    project_ref_array = mp_item_json['spec']['resources']['project_reference_list']
    project_ref_array.append(project_spec)
    mp_item_json['spec']['resources']['project_reference_list'] = project_ref_array
    print mp_item_json['spec']['resources']['project_reference_list']
  else:
    print "Unable to retrieve Marketplace item for uuid: {}".format(mp_item_uuid)
    print "Status Code: {} Response: {}".format(r2.status_code, r2.text)
    exit(1)
    
  url3_method = "PUT"
  r3 = process_request(url3, url3_method, user, password, headers, json.dumps(mp_item_json))
  if r3.ok:
    print "Updating the marketplace item uuid: {} with project: {}".format(mp_item_uuid, "tenant05")
    #print "Update Status Code: {} Response: ".format(r3.status_code. r3.text)
  else:
    print "Unable to update the marketplace_item_uuid: {} with project: {}".format(mp_item_uuid, "tenant05")
    print "Status Code: {} Response: {}".format(r3.status_code, r3.text)
    exit(1)

print "All selected marketplace items were updated successfully with project: {}".format("tenant05")
