sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

echo "** Adding current user to docker group..."
sudo usermod -aG docker @@{Ubuntu Credential.username}@@