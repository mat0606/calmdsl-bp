echo "Starting Nexus services"
sudo systemctl daemon-reload
sudo systemctl start nexus.service
sudo systemctl enable nexus.service
echo "Disabling firewall"
sudo systemctl stop firewalld
sudo systemctl disable firewalld