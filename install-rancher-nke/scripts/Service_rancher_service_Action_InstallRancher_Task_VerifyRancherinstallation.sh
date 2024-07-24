KUBECONFIG=/home/centos/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

kubectl -n cattle-system rollout status deploy/rancher

kubectl -n cattle-system get all