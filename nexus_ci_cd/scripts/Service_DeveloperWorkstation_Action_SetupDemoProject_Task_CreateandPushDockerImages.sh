#!/bin/bash
echo "Hello World"
set -x

export DOCKER_REGISTRY=@@{Nexus_vmname}@@.@@{domain_name}@@
#export DOCKER_REGISTRY=@@{Docker Registry.name}@@.@@{domain_name}@@
export PROJECT_NAME=@@{initial_project_name}@@
echo "Login into Nexus Registry"
#docker login -u @@{Docker Registry Credential.username}@@ -p @@{Docker Registry Credential.secret}@@ $DOCKER_REGISTRY
docker login -u @@{Nexus Jenkins Credential.username}@@ -p @@{Nexus Jenkins Credential.secret}@@ $DOCKER_REGISTRY:@@{Nexus_Repo_Port}@@

cd ~/@@{initial_project_name}@@

echo "Build and Push Ansible Image"
while true ; do
  #docker build -t ${DOCKER_REGISTRY}/@@{initial_project_name}@@/ansible docker-ansible/src
  
  docker build -t ${DOCKER_REGISTRY}:@@{Nexus_Repo_Port}@@/@@{initial_project_name}@@/ansible docker-ansible/src
  if [ $? -eq 0 ]; then
    break
  else
    sleep 15
  fi
done

echo "List out the docker images"
docker images list
echo "Tag the docker images"
docker tag $(docker images | awk '{print $1}' | awk 'NR==2') @@{Nexus_vmname}@@.@@{domain_name}@@:@@{Nexus_Repo_Port}@@/devops/ansible:latest
# docker push ${DOCKER_REGISTRY}:@@{Nexus_Repo_Port}@@/@@{initial_project_name}@@/ansible
echo "Push the docker images into Nexus"
docker push @@{Nexus_vmname}@@.@@{domain_name}@@:@@{Nexus_Repo_Port}@@/devops/ansible:latest
