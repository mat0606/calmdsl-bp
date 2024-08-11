ip = "@@{PC_IP}@@"
user = "@@{PC_Creds.username}@@"
password = "@@{PC_Creds.secret}@@"
object_store_uuid = "@@{object_store_uuid}@@"

bucket_name = "@@{bucket_name}@@"
status_path = "/oss/api/nutanix/v3/objectstores/" + object_store_uuid + "/buckets/" + bucket_name

base_url = "https://" + ip + ":9440"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"

url = base_url + status_path

bucket_create_pending = True

payload = {}
while bucket_create_pending:

  r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
  if r.ok:
    json_resp = r.json()
    if json_resp["status"]["state"] == 'COMPLETE':
      bucket_create_pending = False
      print("Bucket" + bucket_name + " creation is Completed.")
      break
    else:
      print("Bucket creation " + bucket_name + " is in " + json_resp["status"]["state"]) + " state."
      time.sleep(30)
  else:
    print ("Failure in getting bucket creation state")
    print ("Status Code: " + r.status_code + " Response: " + r.text) 
