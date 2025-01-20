#export DOCKER_REGISTRY=@@{Docker Registry.name}@@.@@{domain_name}@@
export DOCKER_REGISTRY=@@{Nexus.vm_name}@@.@@{domain_name}@@
export PROJECT_NAME=@@{new_project_name}@@
echo "Login into Docker Registry"

#docker login -u @@{Docker Registry Credential.username}@@ -p @@{Docker Registry Credential.secret}@@ $DOCKER_REGISTRY
docker login -u @@{Nexus Jenkins Credential.username}@@ -p @@{Nexus Jenkins Credential.secret}@@ $DOCKER_REGISTRY
cd ~/@@{new_project_name}@@

echo "Build and Push Ansible Image"
docker build -t ${DOCKER_REGISTRY}/@@{new_project_name}@@/ansible docker-ansible/src
docker push ${DOCKER_REGISTRY}/@@{new_project_name}@@/ansible
