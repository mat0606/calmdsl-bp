export NKP_VERSION=@@{nkp_version}@@
export CLUSTER_NAME=@@{nkp_cluster_name}@@ 
export NUTANIX_USER=@@{PC Credential.username}@@ 
export NUTANIX_PASSWORD='@@{PC Credential.secret}@@' 
export NUTANIX_ENDPOINT='@@{PC_IP}@@' 
export NUTANIX_PORT=9440 
export CONTROL_PLANE_ENDPOINT_IP='@@{control_plane_endpoint}@@' 
#Ex: 10.42.236.203 
export NUTANIX_MACHINE_TEMPLATE_IMAGE_NAME=@@{nkp_machine_template_name}@@
export NUTANIX_PRISM_ELEMENT_CLUSTER_NAME='@@{cluster_name}@@' 
export NUTANIX_SUBNET_NAME='@@{subnet_name}@@' 
export REGISTRY_MIRROR_URL=@@{registry_mirror_url}@@
export NUTANIX_STORAGE_CONTAINER_NAME=SelfServiceContainer 
export CSI_FILESYSTEM=xfs 
export CSI_ATTACHED=false 
export LB_IP_RANGE='@@{lb_start_ip}@@-@@{lb_end_ip}@@' 

nkp create cluster nutanix -c $CLUSTER_NAME \
    --kind-cluster-image $REGISTRY_MIRROR_URL/mesosphere/konvoy-bootstrap:v$NKP_VERSION \
    --endpoint https://$NUTANIX_ENDPOINT:$NUTANIX_PORT \
    --insecure \
    --kubernetes-service-load-balancer-ip-range $LB_IP_RANGE \
    --control-plane-endpoint-ip $CONTROL_PLANE_ENDPOINT_IP \
    --control-plane-vm-image $NUTANIX_MACHINE_TEMPLATE_IMAGE_NAME \
    --control-plane-prism-element-cluster $NUTANIX_PRISM_ELEMENT_CLUSTER_NAME \
    --control-plane-subnets $NUTANIX_SUBNET_NAME \
    --control-plane-replicas 1 \
    --worker-vm-image $NUTANIX_MACHINE_TEMPLATE_IMAGE_NAME \
    --worker-prism-element-cluster $NUTANIX_PRISM_ELEMENT_CLUSTER_NAME \
    --worker-subnets $NUTANIX_SUBNET_NAME \
    --worker-replicas 3 \
    --csi-storage-container $NUTANIX_STORAGE_CONTAINER_NAME \
    --registry-mirror-url http://$REGISTRY_MIRROR_URL \
    --self-managed

