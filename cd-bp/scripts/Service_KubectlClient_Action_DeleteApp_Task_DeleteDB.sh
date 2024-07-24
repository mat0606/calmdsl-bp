export KUBECONFIG=/home/centos/@@{cluster_name}@@-kubectl.cfg

kubectl delete ns devops@@{build_number}@@
kubectl delete secret mysql-pass
kubectl delete -f db_deploy.yaml