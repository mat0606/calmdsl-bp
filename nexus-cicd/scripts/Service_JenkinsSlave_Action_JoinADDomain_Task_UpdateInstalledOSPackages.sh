#sudo tee -a /etc/apt/sources.list <<EOF
#deb http://us.archive.ubuntu.com/ubuntu/ bionic universe
#deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe
#EOF

echo "List out source repositories to update"
grep -i "^deb" /etc/apt/sources.list

#sudo apt update -y
sudo apt-get update -y
#sudo apt upgrade -y
sudo DEBIAN_FRONTEND=noninteractive apt-get -yq full-upgrade
sudo reboot
