sudo dnf install -y epel-release unzip vim wget net-tools
sudo dnf -y install git yum-utils device-mapper-persistent-data lvm2
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io
sudo docker --version
sudo systemctl start docker
sudo systemctl enable docker
