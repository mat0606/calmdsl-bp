KUBECONFIG=/home/centos/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

# UnInstall the cert-manager Helm chart
helm uninstall cert-manager jetstack/cert-manager --namespace cert-manager 

kubectl delete ns cert-manager