KUBECONFIG=/home/nutanix/@@{nkp_kubeconfig}@@
export KUBECONFIG

helm uninstall rancher rancher-@@{rancher_helm_chart_repo}@@ --namespace cattle-system
kubectl delete ns cattle-system
