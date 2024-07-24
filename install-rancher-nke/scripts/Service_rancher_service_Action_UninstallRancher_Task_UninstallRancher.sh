KUBECONFIG=/home/centos/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

helm uninstall rancher rancher-<CHART_REPO>/rancher --namespace cattle-system
kubectl delete ns cattle-system
