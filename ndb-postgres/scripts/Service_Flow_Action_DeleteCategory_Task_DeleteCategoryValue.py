user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{pc_ip}@@"

def process_request(url, method, user, password, headers, payload=None):
    r = urlreq(url, verb=method, auth="BASIC", user=user, passwd=password, params=payload, verify=False, headers=headers)
    return r

url = "https://" + ip + ":9440/api/nutanix/v3/categories/Environment/@@{calm_application_name}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "DELETE"
r = process_request(url, url_method, user, password, headers)
print "Response Status: " + str(r.status_code)
