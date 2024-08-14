KUBECONFIG=/home/nutanix/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

kubectl -n metallb-system delete deployment.apps/controller
kubectl -n metallb-system delete daemonset.apps/speaker
kubectl -n metallb-system delete service/webhook-service
#kubectl -n metallb-system delete configmap config
kubectl -n metallb-system delete configmap kube-root-ca.crt
kubectl -n metallb-system delete configmap metallb-excludel2
kubectl delete ns metallb-system