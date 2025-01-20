#!/bin/bash
set -x

echo "Install Jenkins Plugins"
echo "http://@@{address}@@:8080"
echo "admin:@@{jenkins_authorization}@@"

#wget -O /tmp/pam-auth.hpi http://updates.jenkins-ci.org/download/plugins/pam-auth/1.4/pam-auth.hpi
#wget -O /tmp/pam-auth.hpi http://updates.jenkins-ci.org/download/plugins/pam-auth/1.8/pam-auth.hpi
wget -O /tmp/pam-auth.hpi http://updates.jenkins-ci.org/download/plugins/pam-auth/1.10/pam-auth.hpi
sudo java -jar jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 install-plugin -deploy file:///tmp/pam-auth.hpi -restart
echo "Sleeping for 30 seconds for Jenkins to restart after installing pam-auth plugin"
sleep 30
sudo java -jar jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 install-plugin -deploy authentication-tokens -restart
echo "Sleeping for 60 seconds for Jenkins to restart after installing authentication-tokens plugin"
sleep 60
#20 May 22 - jackson2 had depnedencies to javax-activation-api:1.2.0-3, jaxb:2.3.6-1, snakeyaml-api:1.29.1
#20 May 22 - jaxb:2.3.6-1 had dependencies to javax-activation-api:1.2.0-3, sshd:3.0.1, javax-mail-api:1.6.2.5
#20 May 22 - snakeyaml-api had dependencies to sshd:3.0.1, javax-mail-api:1.6.2.5
sudo java -jar jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 install-plugin -deploy script-security bouncycastle-api trilead-api http_request javax-activation-api sshd javax-mail-api -restart
sleep 60
while true ; do
  #sudo java -jar jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 install-plugin -deploy authentication-tokens script-security bouncycastle-api http_request jackson2-api jquery-detached jsch ldap mapdb-api momentjs pam-auth nutanix-calm credentials plain-credentials resource-disposer scm-api ssh-credentials ssh-slaves structs subversion timestamper token-macro workflow-api workflow-basic-steps workflow-cps workflow-durable-task-step workflow-job workflow-multibranch workflow-scm-step workflow-step-api workflow-support workflow-aggregator credentials-binding git git-client git-server swarm cloudbees-folder cloudbees-credentials -restart
  #sudo java -jar jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 install-plugin -deploy script-security bouncycastle-api trilead-api http_request jackson2-api jquery-detached jsch ldap mapdb-api momentjs nutanix-calm credentials plain-credentials resource-disposer scm-api ssh-credentials ssh-slaves structs subversion timestamper token-macro workflow-api workflow-basic-steps workflow-cps workflow-durable-task-step workflow-job workflow-multibranch workflow-scm-step workflow-step-api workflow-support workflow-aggregator credentials-binding git git-client git-server swarm cloudbees-folder cloudbees-credentials nexus-artifact-uploader pipeline-utility-steps -restart
  sudo java -jar jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 install-plugin -deploy jaxb snakeyaml-api jackson2-api jquery-detached jsch ldap mapdb-api momentjs nutanix-calm credentials plain-credentials resource-disposer scm-api ssh-credentials ssh-slaves structs subversion timestamper token-macro workflow-api workflow-basic-steps workflow-cps workflow-durable-task-step workflow-job workflow-multibranch workflow-scm-step workflow-step-api workflow-support workflow-aggregator credentials-binding swarm cloudbees-folder cloudbees-credentials nexus-artifact-uploader pipeline-utility-steps -restart
  if [ $? -eq 0 ]; then
    break
  else
    sleep 60
  fi
done
echo "Installing git plugin"
sudo java -jar jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 install-plugin -deploy git git-client git-server
sleep 60
