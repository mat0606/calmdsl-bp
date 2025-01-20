echo "Create SSH Keys"
sudo su -c 'mkdir ~/.ssh' - jenkins
sudo su -c 'chmod 700 ~/.ssh' - jenkins
sudo su -c 'echo "@@{Jenkins Key.secret}@@" > ~/.ssh/id_rsa' - jenkins
sudo su -c 'echo "@@{jenkins_public_key}@@" > ~/.ssh/id_rsa.pub' - jenkins
sudo su -c 'chmod 600 ~/.ssh/id_rsa*' - jenkins
sudo su -c 'echo "set -o vi" > ~/.bashrc' - jenkins
sudo su -c 'echo "StrictHostKeyChecking no" > ~/.ssh/config' - jenkins

echo ""
echo "Get Public Key"
echo "jenkins_ssh_key_pub="$(sudo cat /var/lib/jenkins/.ssh/id_rsa.pub)
