user = "@@{CalmVM Credential.username}@@"
password = "@@{CalmVM Credential.secret}@@"
#ip = "@@{PC_IP}@@"
ip = "@@{CalmVM_IP}@@"


user_reference_list = @@{Tenant_Admin_List}@@
#consumer = {
#  "kind": "user",
#  "name": "@@{Tenant_Consumer}@@",
#  "uuid": "@@{Tenant_Consumer_UUID}@@"
#}
#user_reference_list.append(consumer)
consumer_reference_list = @@{Tenant_Consumer_List}@@
acp_consumer_payload =  {
        "acp": {
          "name": "nuCalmAcp-9bbe7ee0-7c44-4267-a5dd-335703e79b74",
          "resources": {
            "role_reference": {
              "kind": "role",
              "name": "Consumer",
              "uuid": "@@{consumer_role_UUID}@@"
            },
            "user_reference_list": consumer_reference_list,
            "user_group_reference_list": [],
            "filter_list": {
              "context_list": [
                {
                  "scope_filter_expression_list": [
                    {
                      "operator": "IN",
                      "left_hand_side": "PROJECT",
                      "right_hand_side": {
                        "uuid_list": [
                          "@@{Project_UUID}@@"
                        ]
                      }
                    }
                  ],
                  "entity_filter_expression_list": [
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "ALL"
                      },
                      "right_hand_side": {
                        "collection": "ALL"
                      }
                    }
                  ]
                },
                {
                  "entity_filter_expression_list": [
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "image"
                      },
                      "right_hand_side": {
                        "collection": "ALL"
                      }
                    },
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "marketplace_item"
                      },
                      "right_hand_side": {
                        "collection": "SELF_OWNED"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "directory_service"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "role"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "uuid_list": [
                          "@@{Project_UUID}@@"
                        ]
                      },
                      "left_hand_side": {
                        "entity_type": "project"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "user"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "user_group"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "SELF_OWNED"
                      },
                      "left_hand_side": {
                        "entity_type": "environment"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "app_icon"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "category"
                      }
                    },
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "app_task"
                      },
                      "right_hand_side": {
                        "collection": "SELF_OWNED"
                      }
                    },
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "app_variable"
                      },
                      "right_hand_side": {
                        "collection": "SELF_OWNED"
                      }
                    }
                  ]
                }
              ]
            }
          }
        },
        "metadata": {
          "kind": "access_control_policy"
        },
        "operation": "ADD"
      }
  
print ("acp_consumer_payload: " + acp_consumer_payload)
acp_payload = [
      {
        "acp": {
          "name": "nuCalmAcp-cbba4833-50a3-423a-bca7-1eb6e2770a1f",
          "resources": {
            "role_reference": {
              "kind": "role",
              "name": "Project Admin",
              "uuid": "@@{project_admin_role_UUID}@@"
            },
            "user_reference_list": user_reference_list,
            "user_group_reference_list": [],
            "filter_list": {
              "context_list": [
                {
                  "scope_filter_expression_list": [
                    {
                      "operator": "IN",
                      "left_hand_side": "PROJECT",
                      "right_hand_side": {
                        "uuid_list": [
                          "@@{Project_UUID}@@"
                        ]
                      }
                    }
                  ],
                  "entity_filter_expression_list": [
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "ALL"
                      },
                      "right_hand_side": {
                        "collection": "ALL"
                      }
                    }
                  ]
                },
                {
                  "entity_filter_expression_list": [
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "image"
                      },
                      "right_hand_side": {
                        "collection": "ALL"
                      }
                    },
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "marketplace_item"
                      },
                      "right_hand_side": {
                        "collection": "SELF_OWNED"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "directory_service"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "role"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "uuid_list": [
                          "@@{Project_UUID}@@"
                        ]
                      },
                      "left_hand_side": {
                        "entity_type": "project"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "user"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "user_group"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "SELF_OWNED"
                      },
                      "left_hand_side": {
                        "entity_type": "environment"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "app_icon"
                      }
                    },
                    {
                      "operator": "IN",
                      "right_hand_side": {
                        "collection": "ALL"
                      },
                      "left_hand_side": {
                        "entity_type": "category"
                      }
                    },
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "app_task"
                      },
                      "right_hand_side": {
                        "collection": "SELF_OWNED"
                      }
                    },
                    {
                      "operator": "IN",
                      "left_hand_side": {
                        "entity_type": "app_variable"
                      },
                      "right_hand_side": {
                        "collection": "SELF_OWNED"
                      }
                    }
                  ]
                }
              ]
            }
          }
        },
        "metadata": {
          "kind": "access_control_policy"
        },
        "operation": "ADD"
      }, 
      acp_consumer_payload
    ]
 
base_url = "https://" + ip + ":9440/api/nutanix/v3/projects_internal"
url = base_url + "/@@{Project_UUID}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "GET"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, verify=False, headers=headers)
#print "Status Code: {}".format(r.status_code)
print ("Response: " + r.text)
if r.ok:
  project_json = r.json()
  project_json.pop("status", None)
  project_json["spec"]["access_control_policy_list"] = acp_payload

else:
  exit(1)
base_url = "https://" + ip + ":9440/api/nutanix/v3/projects_internal"
url = base_url + "/@@{Project_UUID}@@"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
url_method = "PUT"
r = urlreq(url, url_method, auth="BASIC", user=user, passwd=password, params=json.dumps(project_json), verify=False, headers=headers)
#print "Status code: {}".format(r.status_code)
print ("Response: " + r.text)
if r.ok:
  print ("Addition of users to project is successful")
else:
  exit(1)
