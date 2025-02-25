KUBECONFIG=/home/nutanix/@@{nkp_kubeconfig}@@
export KUBECONFIG

helm repo add rancher-stable https://releases.rancher.com/server-charts/stable

helm repo list

helm install rancher rancher-@@{rancher_helm_chart_repo}@@/rancher \
  --namespace cattle-system \
  --set hostname=rancher.@@{domain_name}@@ \
  --set bootstrapPassword=@@{Rancher Credential.secret}@@