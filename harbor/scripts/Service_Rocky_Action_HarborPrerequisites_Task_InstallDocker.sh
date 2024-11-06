sudo dnf install -y epel-release unzip vim wget net-tools
sudo dnf -y install git yum-utils device-mapper-persistent-data lvm2
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io
sudo docker --version
echo "Installing Docker Compose v2.12.2"
sudo curl -L "https://github.com/docker/compose/releases/download/v2.12.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose
sudo docker-compose --version
sudo systemctl start docker
sudo systemctl enable docker
