

  ## Create the Karbon Kubernetes cluster
  # Set the headers, payload, and cookies
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
worker_node_memory = 1024 * @@{worker_node_memory}@@
worker_node_disk = 1024 * @@{worker_node_disk_size}@@

payload = {
  "cni_config": {
    "node_cidr_mask_size": 24, #Allow up to 255 pods per node
    "pod_ipv4_cidr": "@@{pod_cidr_range}@@",
    "service_ipv4_cidr": "@@{service_cidr_range}@@"
  },
  "etcd_config": {
   
  },
  "masters_config": {
    
  },
  "metadata": {
    "api_version": "v1.0.0"
  },
  "name": "@@{cluster_name}@@",
  "storage_class_config": {
    "default_storage_class": True,
    "name": "default-storageclass",
    "reclaim_policy": "Delete",
    "volumes_config": {
      "file_system": "@@{file_system}@@",
      "flash_mode": False,
    #  "password": "@@{PE_SC_Creds.secret}@@",
      "password": "@@{pe_sc_credential}@@",
    #  "prism_element_cluster_uuid": "@@{PE_Cluster_UUID}@@",
      "prism_element_cluster_uuid": "@@{nutanix_cluster_uuid}@@",
      "storage_container": "@@{Storage_Container}@@",
      "username": "admin"
    }
  },
  "version": "@@{K8S_Version}@@",
  "workers_config": {
    "node_pools": [
    {
      "ahv_config": {
        "cpu": @@{worker_node_cpu}@@,
        "disk_mib": worker_node_disk,
        "memory_mib": worker_node_memory,
        "network_uuid": "@@{SUBNET_UUID}@@",
      #  "prism_element_cluster_uuid": "@@{PE_Cluster_UUID}@@"
        "prism_element_cluster_uuid": "@@{nutanix_cluster_uuid}@@"
      },
      "name": "worker-node-pool",
      "node_os_version": "@@{image_name}@@",
      "num_instances": @@{No_Worker_Node}@@
    }]
  }
}


if ("@@{Kubernetes_Node_Network}@@" == "Flannel"):
  print "Configuring Flannel CNI"
 # payload = json.loads(karbon_config)
  payload['cni_config']['flannel_config'] = {
    "ip_pool_configs": [{
      "cidr": "@@{pod_cidr_range}@@"
    }]
    
  }
  #payload['cni_config'].insert(0, cni)
else:
  print "Configuring Calico CNI"
  #payload = json.loads(karbon_config)
  payload['cni_config']['calico_config'] = {
    "ip_pool_configs": [{
      "cidr": "@@{calico_cidr}@@"
    }]
    
  }
  #payload['cni_config'].insert(0, cni)
if ("@@{Master_Config}@@" == "Single Master"):
  print "Configuring Single Master"
  master_pool = {
    "node_pools": [
    {
      "ahv_config": {
        "cpu": 2,
        "disk_mib": 122880,
        "memory_mib": 4096,
        "network_uuid": "@@{SUBNET_UUID}@@",
       # "prism_element_cluster_uuid": "@@{PE_Cluster_UUID}@@"
        "prism_element_cluster_uuid": "@@{nutanix_cluster_uuid}@@"
      },
      "name": "master-node-pool", #name of the node pool
      "node_os_version": "@@{image_name}@@",
      "num_instances": 1
    }],
    "single_master_config": { 
      "external_ipv4_address": "@@{Master_VIP}@@"
    }
  }
  payload['masters_config'] = master_pool  
  etcd_pool = {
    "node_pools": [
    {
      "ahv_config": {
        "cpu": 2,
        "disk_mib": 40960,
        "memory_mib": 8192,
        "network_uuid": "@@{SUBNET_UUID}@@",
       # "prism_element_cluster_uuid": "@@{PE_Cluster_UUID}@@"
        "prism_element_cluster_uuid": "@@{nutanix_cluster_uuid}@@"
      },
      "name": "etcd-node-pool", #name of the node pool
      "node_os_version": "@@{image_name}@@",
      "num_instances": 1
    }]
  }
  payload['etcd_config'] = etcd_pool
elif ("@@{Master_Config}@@" == "Active-Passive"):
  print "Configuring Active-Passive Master"
  master_pool = { 
    "active_passive_config": {
      "external_ipv4_address": "@@{Master_VIP}@@"
    },
    "node_pools": [
    {
      "ahv_config": {
        "cpu": 2,
        "disk_mib": 122880,
        "memory_mib": 4096,
        "network_uuid": "@@{SUBNET_UUID}@@",
      #  "prism_element_cluster_uuid": "@@{PE_Cluster_UUID}@@"
        "prism_element_cluster_uuid": "@@{nutanix_cluster_uuid}@@"
      },
      "name": "master-node-pool", #name of the node pool
      "node_os_version": "@@{image_name}@@",
      "num_instances": 2
    }]
  }
  payload['masters_config'] = master_pool
  etcd_pool = {
    "node_pools": [
    {
      "ahv_config": {
        "cpu": 2,
        "disk_mib": 40960,
        "memory_mib": 8192,
        "network_uuid": "@@{SUBNET_UUID}@@",
       # "prism_element_cluster_uuid": "@@{PE_Cluster_UUID}@@"
        "prism_element_cluster_uuid": "@@{nutanix_cluster_uuid}@@"
      },
      "name": "etcd-node-pool", #name of the node pool
      "node_os_version": "@@{image_name}@@",
      "num_instances": 3
    }]
  }
  payload['etcd_config'] = etcd_pool
else:
  print "Configuring Active-Active LoadBalancer Master"
  master_pool = {
    "external_lb_config": {
      "external_ipv4_address": "@@{External_LB}@@",
      "master_nodes_config": [
      {
        "ipv4_address": "@@{Master_VIP}@@",
        "node_pool_name": "@@{cluster_name}@@"
      },
      {
        "ipv4_address": "@@{Master_VIP2}@@",
        "node_pool_name": "@@{cluster_name}@@"
      }
    ]},
    "node_pools": [
    {
      "ahv_config": {
        "cpu": 2,
        "disk_mib": 122880,
        "memory_mib": 4096,
        "network_uuid": "@@{SUBNET_UUID}@@",
       # "prism_element_cluster_uuid": "@@{PE_Cluster_UUID}@@"
        "prism_element_cluster_uuid": "@@{nutanix_cluster_uuid}@@"
      },
      "name": "master-node-pool", #name of the node pool
      "node_os_version": "@@{image_name}@@",
      "num_instances": 2
    }]
  }
  payload['masters_config'] = master_pool
  etcd_pool = {
    "node_pools": [
    {
      "ahv_config": {
        "cpu": 2,
        "disk_mib": 40960,
        "memory_mib": 8192,
        "network_uuid": "@@{SUBNET_UUID}@@",
       # "prism_element_cluster_uuid": "@@{PE_Cluster_UUID}@@"
        "prism_element_cluster_uuid": "@@{nutanix_cluster_uuid}@@"
      },
      "name": "etcd-node-pool", #name of the node pool
      "node_os_version": "@@{image_name}@@",
      "num_instances": 3
    }]  
  }
  payload['etcd_config'] = etcd_pool
print json.dumps(payload)

  
pc_user = '@@{PC_Creds.username}@@'
pc_pass = '@@{PC_Creds.secret}@@'


  # Set the address and make images call
#url = "https://localhost:9440/karbon/v1/k8s/clusters"
url = "https://@@{PC_IP}@@:9440/karbon/v1/k8s/clusters"

resp = urlreq(url, verb='POST',params=json.dumps(payload), headers=headers, auth='BASIC', user=pc_user, passwd=pc_pass, verify=False)

  # If the call went through successfully, find the image by name
if resp.ok:
  print "Cluster create was successful", json.dumps(json.loads(resp.content), indent=4)
  exit(0)

  # If the call failed
else:
  print "Cluster create failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)

