nslookup @@{name}@@.@@{domain_name}@@
echo "Installing SSH Pass"
sudo apt install -y sshpass

GITOLITE_IP=@@{name}@@.@@{domain_name}@@
#sshpass -p @@{Nexus Credential 2.secret}@@ scp -oStrictHostKeyChecking=no centos@${REGISTRY_IP}:~/nexus_server.pem /tmp
echo "Copy a file from Gitolite for ECDSA Host Key verification"
export SSHPASS=@@{Ubuntu Credential.secret}@@
sshpass -e scp -oStrictHostKeyChecking=no git@${GITOLITE_IP}:~/.profile /tmp
