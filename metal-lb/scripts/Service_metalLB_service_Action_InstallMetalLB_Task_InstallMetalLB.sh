KUBECONFIG=/home/nutanix/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
export KUBECONFIG

# For version 0.12.1 & below
#kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v@@{MetalLB_version}@@/manifests/namespace.yaml
#kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v@@{MetalLB_version}@@/manifests/metallb.yaml

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v@@{MetalLB_version}@@/config/manifests/metallb-native.yaml

# On first install only
kubectl create secret generic -n metallb-system memberlist --from-literal=secretkey="$(openssl rand -base64 128)"

