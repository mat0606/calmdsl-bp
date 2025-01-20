user = "@@{Prism Central User.username}@@"
password = "@@{Prism Central User.secret}@@"

def process_request(url, method, user, password, headers, payload=None):
    r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
    return r

url = "https://@@{pc_instance_ip}@@:9440/api/nutanix/v3/blueprints/list"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"
payload = {"filter": "name==@@{new_app_deploy_blueprint}@@"}
r = process_request(url, url_method, user, password, headers, json.dumps(payload))
print ("Response Status: " + str(r.status_code))
print ("Response: " + r.json())
app_deploy_blueprint_uuid = r.json()['entities'][0]['status']['uuid']
print ("App Blueprint UUID: " + app_deploy_blueprint_uuid)

#bp_uuid = ''
#for entity in r.json()['entities']:
#    if entity['status']['name'] == "@@{new_app_deploy_blueprint}@@":
#        bp_uuid = entity['status']['uuid']

url_method = 'GET'
url = "https://@@{pc_instance_ip}@@:9440/api/nutanix/v3/blueprints/" + app_deploy_blueprint_uuid
r = process_request(url, url_method, user, password, headers, payload)
print "Response Status: " + str(r.status_code)
for profile in r.json()['spec']['resources']['app_profile_list']:
    if profile['name'] == 'Default':
        app_profile_uuid = profile['uuid']
       
print ("App Profile UUID: " + app_profile_uuid)

print ("app_deploy_blueprint_uuid=" + app_deploy_blueprint_uuid)
print ("app_profile_uuid=" + app_profile_uuid)
