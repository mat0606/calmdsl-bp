user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"

# filter by name because AOS 6.8 with PC2024.1 subnet list api failed without this name filter 
payload = {
}
#base_url = "https://" + ip + ":9440/api/nutanix/v3/categories"
#url = base_url + "/list"
limit = 100
page = 1
orderBy = "key"
url = "https://" + ip + ":9440/api/prism/v4.0/config/categories?$page=" + str(page) + "&$limit=" + str(limit) + "&$orderby=" + orderBy
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
#print ("Status code: " + str(r.status_code))
#print ("Output: " + r.text)
categories_list = []
categories_list_json = r.json()
for category in categories_list_json['data']:
  #print (category['name'])
  categories_list.append(category['key'])
unique_list = list(set(categories_list))
print (','.join(unique_list))