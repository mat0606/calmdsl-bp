echo "No longer in use"
#sudo apt install -y curl

#sudo apt-get -y remove docker docker-engine docker.io containerd runc

#echo "** Downloading Docker Repo Key..."
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

#echo "** Adding Docker Repo..."
#sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

#echo "** Apt Update..."
#sudo apt-get install -y sshpass

#echo "** Set apt-cache policy for docker-ce..."
#apt-cache policy docker-ce

#echo "** Installing Docker CE..."
#sudo apt-get install -y docker-ce docker-ce-cli containerd.io

#echo "** Adding current user to docker group..."
#sudo usermod -aG docker @@{Ubuntu Credential.username}@@
