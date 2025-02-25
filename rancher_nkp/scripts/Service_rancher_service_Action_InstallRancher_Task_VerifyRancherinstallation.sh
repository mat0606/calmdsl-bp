KUBECONFIG=/home/nutanix/@@{nkp_kubeconfig}@@
export KUBECONFIG

kubectl -n cattle-system rollout status deploy/rancher

kubectl -n cattle-system get all