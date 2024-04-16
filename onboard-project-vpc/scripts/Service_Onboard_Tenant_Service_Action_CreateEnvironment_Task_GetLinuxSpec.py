cred_uuid = "{}".format(str(uuid.uuid4())) # Centos Credential uuid
cred2_uuid = "{}".format(str(uuid.uuid4())) # Centos 2 Credential uuid
subtrate_uuid = "{}".format(str(uuid.uuid4()))

ip_str = "@"+"@" + "{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}"+ "@"+"@"

guest_customization_data = {
  "cloud_init": {
    "meta_data": "",
    "type": "",
    "user_data": "#cloud-config\ndisable_root: False\nssh_enabled: True\nssh_pwauth: False\nusers:\n  - name: centos\n    ssh-authorized-keys:\n      - @@{CENTOS.public_key}@@\n    sudo: ['ALL=(ALL) NOPASSWD:ALL']"
  },
  "type": ""
  #"sysprep": None
}



LINUX_SPEC = {
  "uuid": subtrate_uuid,
  "action_list": [],
  "readiness_probe": {
    "connection_type": "SSH",
    "connection_port": 22,
   # "address": ip_str,
    "delay_secs": "60",
    "disable_readiness_probe": True, #False,
    "login_credential_local_reference": {
      "kind": "app_credential",
      "uuid": cred_uuid
    }
  },
  "editables": {
  },
  "os_type": "Linux",
  "type": "AHV_VM",
  "create_spec": {
    "name": "vm-@@{calm_array_index}@@-@@{calm_time}@@",
    "categories": "",
   # "availability_zone_reference": null,
   # "backup_policy": null,
    "type": "",
    "cluster_reference": {
      "kind": "cluster",
      "type": "",
      "name": "@@{Cluster_Name}@@", #"SGNTNXWLPE_AZ01",
      "uuid": "@@{cluster_uuid}@@"#"0005e085-b472-5a84-1ebd-ac1f6b3b4778"
    },
    "resources": {
      "nic_list": [
      {
        "nic_type": "NORMAL_NIC",
        "vpc_reference": {
          "kind": "vpc",
          "type": "",
          "name": "@@{vpc_name}@@",
          "uuid": "@@{vpc_uuid}@@", #"c63b91b1-28a5-4483-b8fd-62b15336b7cc"
        },
        "ip_endpoint_list": [],
      #  "network_function_chain_reference": null,
        "network_function_nic_type": "INGRESS",
        "mac_address": "",
        "subnet_reference": {
          "kind": "subnet",
          "type": "",
          "name": "@@{PE_Network}@@",
          "uuid": "@@{pe_network_UUID}@@", #af8a2252-265e-475b-bdb4-99df17002121"
        },
        "type": ""
      }],
   #   "parent_reference": null,
    #  "guest_tools": null,
      "num_vcpus_per_socket": 1,
      "num_sockets": 2,
      "serial_port_list": [],
      "gpu_list": [],
      "memory_size_mib": 2048,
      "power_state": "ON",
      "hardware_clock_timezone": "",
      "guest_customization": guest_customization_data,
      "type": "",
      "account_uuid": "@@{cluster_account_reference_UUID}@@", #"7862442b-7d23-4f7a-811e-578434b861f5",
      "boot_config": {
        "boot_device": {
          "type": "",
          "disk_address": {
            "adapter_type": "SCSI",
            "device_index": 0,
            "type": ""
          }
        },
        "type": "",
        "boot_type": "LEGACY",
        "mac_address": ""
      },
      "disk_list": [
      {
        "data_source_reference": {
          "kind": "image",
          "type": "",
          "name": "@@{env_image}@@", #"centos7-calm-template.qcow2",
          "uuid": "@@{image_UUID}@@" #"c0e976ed-0288-4870-8338-9521836a3d61"
        },
        "type": "",
        "disk_size_mib": 0,
     #   "volume_group_reference": null,
        "device_properties": {
          "type": "",
          "device_type": "DISK",
          "disk_address": {
            "adapter_type": "SCSI",
            "device_index": 0,
            "type": ""
          }
        }
      }]
    }
  },
  "variable_list": [],
  "name": "Untitled"
}
print "LINUX_SPEC={}".format(LINUX_SPEC)
print "cred_uuid={}".format(cred_uuid)
print "cred2_uuid={}".format(cred2_uuid)
print "subtrate_uuid={}".format(subtrate_uuid)