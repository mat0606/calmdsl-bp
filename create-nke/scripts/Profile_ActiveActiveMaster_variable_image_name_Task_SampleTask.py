user = "@@{PC_Creds.username}@@"
password = "@@{PC_Creds.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
  "kind": "image",
  "sort_order": "DESCENDING",
  "sort_attribute": "name"
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/images"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)

image_list = []
image_list_json = r.json()
for image in image_list_json['entities']:
  if 'ntnx-' in image['spec']['name'] and 'msp' not in image['spec']['name']: #sometimes this value will be '{}'
    image_name = image['spec']['name']
    image_name = image_name.replace('karbon-','')
    image_list.append(image_name)

#print ','.join(image_list)
print (",".join(image_list)) 