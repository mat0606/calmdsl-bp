user = "@@{PC Credential.username}@@"
password = "@@{PC Credential.secret}@@"
ip = "@@{PC_IP}@@"

payload = {
 
}

url = "https://" + ip + ":9440/api/prism/v4.0/config/tasks/@@{task_uuid}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
count = 0
while (count < 6):
  r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(payload), verify=False, headers=headers)
  print ("Status code: " + str(r.status_code))
  print ("Output: " + r.text)
  for task in r.json()['data']:
    if (task['status'] == 'RUNNING'): 
      print ("Task is in RUNNING state.  Sleep for 10 seconds")
      sleep(10)
    elif (task['status'] == 'SUCCEEDED'):
      print ("Task is in SUCCESS state.")
      exit(0)
    elif (task['status'] == 'FAILED'):
      print ("Task failed.")
      exit(1)  
    else:
      print ("Task status: " + task['status'] + " Sleep for 10 seconds")
      sleep(10)
  count = count + 1
else:
  exit(1)