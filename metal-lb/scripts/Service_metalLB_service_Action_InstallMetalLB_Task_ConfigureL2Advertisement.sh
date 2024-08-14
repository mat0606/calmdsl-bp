KUBECONFIG=/home/nutanix/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

echo "Installing L2Advertisement"

echo "
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: empty
  namespace: metallb-system" > metallb-advertisement-config.yaml
  
kubectl apply -f metallb-advertisement-config.yaml
