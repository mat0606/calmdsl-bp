KUBECONFIG=/home/centos/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

kubectl get pods --namespace cert-manager