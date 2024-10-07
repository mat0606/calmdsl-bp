export CLUSTER_NAME=@@{nkp_cluster_name}@@
export NUTANIX_USER=@@{PC Credential.username}@@
export NUTANIX_PASSWORD='@@{PC Credential.secret}@@' 
export NUTANIX_ENDPOINT='@@{PC_IP}@@' 
export NUTANIX_PORT=9440 
export NUTANIX_PRISM_ELEMENT_CLUSTER_NAME='@@{cluster_name}@@' 
export KUBECONFIG=/home/nutanix/@@{nkp_cluster_name}@@.conf
echo "Get Management Cluster nodes"
kubectl get nodes

echo "Deleting the NKP management cluster "
nkp delete cluster -c $CLUSTER_NAME \
     --self-managed

