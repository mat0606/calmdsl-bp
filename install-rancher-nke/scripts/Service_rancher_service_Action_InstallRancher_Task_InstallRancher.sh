KUBECONFIG=/home/centos/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

helm repo add rancher-stable https://releases.rancher.com/server-charts/stable

helm repo list

helm install rancher rancher-@@{rancher_helm_chart_repo}@@/rancher \
  --namespace cattle-system \
  --set hostname=rancher.my.org \
  --set bootstrapPassword=@@{Rancher Credential.secret}@@