#Install K9s
wget https://github.com/derailed/k9s/releases/latest/download/k9s_Linux_amd64.tar.gz
tar zxvf k9s_Linux_amd64.tar.gz 
sudo mv k9s /usr/local/bin

#Refreshes current terminal with all the above
source ~/.bashrc