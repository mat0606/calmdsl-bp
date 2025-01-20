set -x

#mkdir ~/.ssh
#chmod 700 ~/.ssh
# Due to a bug in Calm 3.5.0, I was unable to use the credential macro to output the private key in the correct format
#echo @@{Nutanix Key.secret}@@ > ~/.ssh/id_rsa

#echo "@@{Nutanix Key.secret}@@" | tee ~/.ssh/id_rsa
#chmod 600 ~/.ssh/id_rsa
#echo @@{nutanix_public_key}@@ > ~/.ssh/id_rsa.pub
#chmod 600 ~/.ssh/id_rsa.pub

echo "Installing SSH Pass"
sudo apt install -y sshpass
echo "Make directory to store Nexus certificate"
sudo mkdir /etc/docker/certs.d
cd /etc/docker/certs.d
sudo mkdir @@{Nexus_vmname}@@.@@{domain_name}@@:@@{Nexus.Nexus_Repo_Port}@@
echo "Successfully created the directory to store Nexus certificate.  Going to copy the nexus_server.pem from Nexus OSS VM"

#REGISTRY_IP=@@{Docker Registry.address}@@
REGISTRY_IP=@@{Nexus_vmname}@@.@@{domain_name}@@
#sshpass -p @@{Nexus Credential 2.secret}@@ scp -oStrictHostKeyChecking=no centos@${REGISTRY_IP}:~/nexus_server.pem /tmp
export SSHPASS=@@{Nexus Credential 2.secret}@@
sshpass -e scp -oStrictHostKeyChecking=no centos@${REGISTRY_IP}:~/nexus_server.pem /tmp
echo "Testing for existence of /tmp/nexus_server.pem in the Jenkins slave"
test -f /tmp/nexus_server.pem && echo "Successfully copied the nexus_server.pem from Nexus OSS to the Jenkins slave" || exit 1
sudo mv /tmp/nexus_server.pem /etc/docker/certs.d/@@{Nexus_vmname}@@.@@{domain_name}@@:@@{Nexus_Repo_Port}@@
echo "Successfully moving the nexus_server.pem to /etc/docker/certs.d/@@{Nexus_vmname}@@.@@{domain_name}@@:@@{Nexus_Repo_Port}@@"
cd /etc/docker/certs.d/@@{Nexus_vmname}@@.@@{domain_name}@@:@@{Nexus_Repo_Port}@@
echo "Change file name from nexus_server.pem to nexus_server.crt"

sudo mv nexus_server.pem nexus_server.crt

echo "Verify Nexus certificate"

sudo ls -la /etc/docker/certs.d/@@{Nexus_vmname}@@.@@{domain_name}@@:@@{Nexus_Repo_Port}@@

echo "Update CA Certificate and Restart Nexus to trust the certificate"
sudo update-ca-certificates
sudo service docker restart
echo "@@{Nexus.address}@@ @@{Nexus_vmname}@@.@@{domain_name}@@ @@{Nexus_vmname}@@" | sudo tee -a /etc/hosts
#echo "@@{Docker Registry.address}@@ @@{Docker Registry.name}@@.@@{domain_name}@@ @@{Docker Registry.name}@@" | sudo tee -a /etc/hosts
echo "@@{Gitolite.address}@@ @@{Gitolite.name}@@.@@{domain_name}@@ @@{Gitolite.name}@@" | sudo tee -a /etc/hosts
#echo "@@{Artifactory.address}@@ artifactory.@@{domain_name}@@ artifactory" | sudo tee -a /etc/hosts
