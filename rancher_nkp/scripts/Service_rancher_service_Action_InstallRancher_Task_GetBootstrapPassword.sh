KUBECONFIG=/home/nutanix/@@{nkp_kubeconfig}@@
export KUBECONFIG
kubectl get secret --namespace cattle-system bootstrap-secret -o go-template='{{.data.bootstrapPassword|base64decode}}{{ "\n" }}'