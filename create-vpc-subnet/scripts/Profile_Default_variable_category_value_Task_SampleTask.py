user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"

# filter by name because AOS 6.8 with PC2024.1 subnet list api failed without this name filter 
payload = {

}
#base_url = "https://" + ip + ":9440/api/nutanix/v3/categories/@@{category}@@"
#url = base_url + "/list"
url = "https://" + ip + ":9440/api/prism/v4.0/config/categories?$filter=key eq '@@{category}@@'"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print ("Status code: " + str(r.status_code))
#print ("Output: " + r.text)
categories_value_list = []
categories_value_list_json = r.json()
for category_value in categories_value_list_json['data']:
  #print (category_value['value'])
  categories_value_list.append(category_value['value'])
print (','.join(categories_value_list))