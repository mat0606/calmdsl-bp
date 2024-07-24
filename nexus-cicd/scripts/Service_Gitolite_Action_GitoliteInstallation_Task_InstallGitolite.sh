#source <(sudo cat /etc/bash.bashrc) Issue running this command with calm.  Can run this command from putty
#source ~/.profile
sudo apt install -y git curl
sudo su -c 'export PATH=$PATH:~/bin' - git
sudo su -c 'git clone https://github.com/sitaramc/gitolite' - git
sudo su -c 'gitolite/install -ln' - git
echo "Installing gitolite using nutanix public key"
sudo su -c 'gitolite setup -pk /tmp/nutanix.pub' - git
git clone git@@@{address}@@:gitolite-admin.git
