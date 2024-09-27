items = "@@{MarketPlace_item}@@"
selected_marketplace_items = items.split(",")
print (selected_marketplace_items)

user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
#ip = "@@{PC_IP}@@"
ip = "@@{CalmVM_IP}@@"

def process_request(url, method, user, password, headers, payload=None):
  r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
  return r


selected_marketplace_items_uuid = []
  
for selected_mp_item in selected_marketplace_items:
  
 # mpi_name_filter = "'name==" + selected_mp_item + "'"
  #print "mpi_name_filter: {}".format(mpi_name_filter)
  payload = {
    #"filter": mpi_name_filter,
    "filter": "app_state==PUBLISHED",
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
  #print "Status: {}".format(r.status_code)
  print ("Response: " + r.text)
  
  if r.ok:
    calm_marketplace_list_json = r.json()
    for calm_marketplace_item in calm_marketplace_list_json['entities']:
      if calm_marketplace_item['metadata']['name'] == selected_mp_item:
        print ("name: " +  selected_mp_item + " uuid: " + calm_marketplace_item['metadata']['uuid'])
        selected_marketplace_items_uuid.append(calm_marketplace_item['metadata']['uuid'])
  else:
    print ("Unable to list Marketplace Items")
    print "Status Code: " + str(r.status_code) + " Response: " + r.text)
    exit(1)
  
print ("selected mpi uuid: " + selected_marketplace_items_uuid)

url_method = "GET"
payload2 = {}
project_spec = {
    "kind": "project",
    "name": "@@{Project_name}@@",
    "uuid": "@@{Project_UUID}@@"
  }

print ("Adding project spec to mp: " + project_spec)
for mp_item_uuid in selected_marketplace_items_uuid:
  
  url3 = base_url + "/" + mp_item_uuid
  r2 = process_request(url3, url_method, user, password, headers, json.dumps(payload2))
  if r2.ok:
    mp_item_json = r2.json()
    mp_item_json.pop("status", None) 
    project_ref_array = mp_item_json['spec']['resources']['project_reference_list']
    project_ref_array.append(project_spec)
    mp_item_json['spec']['resources']['project_reference_list'] = project_ref_array
    print (mp_item_json['spec']['resources']['project_reference_list'])
  else:
    print ("Unable to retrieve Marketplace item for uuid: " + mp_item_uuid)
    print ("Status Code: " + str(r2.status_code) + " Response: " + r2.text)
    exit(1)
    
  url3_method = "PUT"
  r3 = process_request(url3, url3_method, user, password, headers, json.dumps(mp_item_json))
  if r3.ok:
    print ("Updating the marketplace item uuid: " + mp_item_uuid + " with project: @@{Project_name}@@")
    #print "Update Status Code: {} Response: ".format(r3.status_code. r3.text)
  else:
    print ("Unable to update the marketplace_item_uuid: " + mp_item_uuid + " with project: @@{Project_name}@@")
    print ("Status Code: " + str(r3.status_code) + " Response: " + r3.text)
    exit(1)

print ("All selected marketplace items were updated successfully with project: @@{Project_name}@@")