KUBECONFIG=/home/nutanix/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

#echo "
#apiVersion: v1
#kind: ConfigMap
#metadata:
#  namespace: metallb-system
#  name: config
#data:
#  config: |
#    address-pools:
#    - name: default
#      protocol: layer2
#      addresses:
#      - @@{Start_IP}@@-@@{End_IP}@@" > metallb-config.yaml
      
#kubectl apply -f metallb-config.yaml

echo "Configuring Layer 2 IP address Pool"

echo "
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: cheap
  namespace: metallb-system
spec:
  addresses:
  - @@{Start_IP}@@-@@{End_IP}@@
" > metallb-ip-pool.yaml

kubectl apply -f metallb-ip-pool.yaml




