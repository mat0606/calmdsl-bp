KUBECONFIG=/home/centos/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

kubectl create namespace cattle-system