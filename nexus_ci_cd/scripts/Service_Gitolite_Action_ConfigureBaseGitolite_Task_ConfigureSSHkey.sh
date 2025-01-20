echo "This task is no longer required because the ssh key is already in the disk image"
#sudo apt-get update
# mkdir ~/.ssh
# chmod 700 ~/.ssh
# echo 'set -o vi' >> ~/.bashrc
# echo 'StrictHostKeyChecking no' > ~/.ssh/config

#echo "Create SSH Keys"
#echo "@@{Nutanix Key.secret}@@" > ~/.ssh/id_rsa
#echo "@@{nutanix_public_key}@@" > ~/.ssh/id_rsa.pub

# chmod 600 ~/.ssh/id_rsa*
# cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys
# cp ~/.ssh/id_rsa.pub /tmp/nutanix.pub
#chmod 644 /tmp/nutanix.pub