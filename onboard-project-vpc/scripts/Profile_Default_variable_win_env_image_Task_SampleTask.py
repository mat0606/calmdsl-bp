user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
  "kind": "image",
  "sort_order": "ASCENDING",
  "sort_attribute": "name",
  "length": 250
}
base_url = "https://" + ip + ":9440/api/nutanix/v3/images"
url = base_url + "/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
image_list = []
image_list_json = r.json()
for image in image_list_json['entities']:
  if image['spec']: #sometimes this value will be '{}'
    image_list.append("{}".format(image['spec']['name']))
print (','.join(image_list))
