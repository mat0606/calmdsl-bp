user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
 
}


url = "https://" + ip + ":9440/api/prism/v4.0/config/tasks/@@{task_uuid}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
print ("Status code: " + str(r.status_code))
print ("Output: " + r.text)
count = 0;
if r.ok:
  while (count < 6):

    if (r.json()['data']['status'] == 'RUNNING'): 
      print ("Task is in RUNNING state.  Sleep for 10 seconds")
      sleep(10)
    elif (r.json()['data']['status'] == 'SUCCEEDED'):
      print ("Task is in SUCCESS state.")
      exit(0)
    elif (r.json()['data']['status'] == 'FAILED'):
      print ("Task failed.")
      exit(1)  
    else:
      print ("Task status" + r.json()['data']['status'])
    r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
    count = count + 1
else:
  exit(1)