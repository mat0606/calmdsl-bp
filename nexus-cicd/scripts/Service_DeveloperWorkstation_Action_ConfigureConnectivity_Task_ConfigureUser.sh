sudo apt-get update
mkdir ~/.ssh
chmod 700 ~/.ssh
echo 'set -o vi' >> ~/.bashrc
#echo 'export DOCKER_REGISTRY=@@{Docker Registry.name}@@.@@{domain_name}@@' >> ~/.bashrc
echo 'export DOCKER_REGISTRY=@@{Nexus_vmname}@@.@@{domain_name}@@' >> ~/.bashrc
echo 'StrictHostKeyChecking no' > ~/.ssh/config

echo "Create SSH Keys"
echo "@@{Nutanix Key.secret}@@" > ~/.ssh/id_rsa
echo "@@{nutanix_public_key}@@" > ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/id_rsa*
