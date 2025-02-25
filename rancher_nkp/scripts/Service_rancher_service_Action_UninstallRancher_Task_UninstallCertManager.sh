KUBECONFIG=/home/nutanix/@@{nkp_kubeconfig}@@
export KUBECONFIG

# UnInstall the cert-manager Helm chart
#helm uninstall cert-manager jetstack/cert-manager --namespace cert-manager 
helm uninstall cert-manager --namespace cert-manager 

kubectl delete ns cert-manager