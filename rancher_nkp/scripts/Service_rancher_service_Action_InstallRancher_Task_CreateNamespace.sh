KUBECONFIG=/home/nutanix/@@{nkp_kubeconfig}@@
export KUBECONFIG
kubectl get nodes
kubectl create namespace cattle-system