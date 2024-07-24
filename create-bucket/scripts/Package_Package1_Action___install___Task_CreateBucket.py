ip = "@@{PC_IP}@@"
user = "@@{PC_Creds.username}@@"
password = "@@{PC_Creds.secret}@@"

VERSIONING_FEATURE = "VERSIONING"

object_store_uuid = "@@{object_store_uuid}@@"
bucket_name = "@@{bucket_name}@@"
enable_versioning = "@@{enable_versioning}@@"

if "@@{non_current_version_expiration}@@" > 0:
  non_current_version_expiration = @@{non_current_version_expiration}@@
  expiration = @@{non_current_version_expiration}@@
else:
  non_current_version_expiration = None #days
  expiration = None #days

base_url = "https://" + ip + ":9440"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "POST"


create_path = "/oss/api/nutanix/v3/objectstores/{}/buckets".format(object_store_uuid)
url = base_url + create_path

create_payload = {
  "api_version": "3.0",
  "metadata": {
    "kind": "bucket"
  },
  "spec": {
    "description": "",
    "name": bucket_name,
    "resources": {
      "features": [
      ]
    }
  }
}

if enable_versioning:
  create_payload["spec"]["resources"]["features"].append(VERSIONING_FEATURE)

if non_current_version_expiration or expiration:
  create_payload["spec"]["resources"]["lifecycle_configuration"] = {
    "Rule": [
    {
      "Filter": {
      },
      "ID": "ntnx-frontend-emptyprefix-rule",
      "Status": "Enabled"
    }
    ]
  }

if non_current_version_expiration:
  create_payload["spec"]["resources"]["lifecycle_configuration"]["Rule"][0]["NoncurrentVersionExpiration"] = {"NoncurrentDays": non_current_version_expiration}

if expiration:
  create_payload["spec"]["resources"]["lifecycle_configuration"]["Rule"][0]["Expiration"] = {"Days": expiration}

    
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(create_payload), verify=False, headers=headers)

if r.ok:
  print "Bucket Creation in Progress", json.dumps(json.loads(r.content), indent=4)
  exit(0)

  # If the call failed
else:
  print "Bucket Creation Failed", json.dumps(json.loads(r.content), indent=4)
  exit(1)

