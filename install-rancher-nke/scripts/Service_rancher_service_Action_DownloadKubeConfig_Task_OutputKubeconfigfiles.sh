rm /home/centos/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg
echo "
# -*- mode: yaml; -*-
# vim: syntax=yaml
#
apiVersion: v1
kind: Config
clusters:
- name: @@{SRC_KUBE_CONTEXT}@@
  cluster:
    @@{src_server}@@
    @@{src_ca}@@ 
users:
- name: default-user-@@{SRC_KUBE_CONTEXT}@@
  user:
    @@{src_token}@@
contexts:
- context:
    cluster: @@{SRC_KUBE_CONTEXT}@@
    user: default-user-@@{SRC_KUBE_CONTEXT}@@
  name: @@{SRC_KUBE_CONTEXT}@@-context
current-context: @@{SRC_KUBE_CONTEXT}@@-context" > /home/centos/@@{SRC_KUBE_CONTEXT}@@-kubectl.cfg

#echo @@{src_kubeconfig}@@ > @@{SRC_KUBECONFIG_name}@@
#echo @@{dst_kubeconfig}@@ > @@{DST_KUBECONFIG_name}@@

