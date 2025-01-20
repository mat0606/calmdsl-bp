echo "Gitolite installed: " + @@{Gitolite.gitolite_installed}@@
nslookup @@{GitoliteVM.name}@@.@@{domain_name}@@
echo "Installing SSH Pass"
sudo apt install -y sshpass

GITOLITE_IP=@@{GitoliteVM.name}@@.@@{domain_name}@@
#sshpass -p @@{Nexus Credential 2.secret}@@ scp -oStrictHostKeyChecking=no centos@${REGISTRY_IP}:~/nexus_server.pem /tmp
echo "Copy a file from Gitolite for ECDSA Host Key verification"
export SSHPASS=@@{Ubuntu Credential.secret}@@
sshpass -e scp -oStrictHostKeyChecking=no @@{Ubuntu Credential.username}@@@${GITOLITE_IP}:~/readme /tmp
echo "gitolite installed: " + @@{Gitolite.gitolite_installed}@@
#sshpass -e scp -oStrictHostKeyChecking=no git@${GITOLITE_IP}:~/.gitolite.rc /tmp
