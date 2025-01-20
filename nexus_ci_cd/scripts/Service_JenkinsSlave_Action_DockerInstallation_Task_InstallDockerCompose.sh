#sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#sudo curl -L "https://github.com/docker/compose/releases/tag/@@{docker_compose_version}@@/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#sudo chmod +x /usr/local/bin/docker-compose
#docker-compose --version

echo "No longer in use"
#sudo apt-get install -y docker-compose-plugin
#apt-cache madison docker-compose-plugin
#sudo apt-get install -y docker-compose-plugin=@@{docker_compose_version}@@~ubuntu-focal
#docker compose version