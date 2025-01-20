# Upgrade to latest version of nodejs
#curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
#sudo bash nodesource_setup.sh
#sudo apt-get install -y nodejs
#sudo apt-get install -y curl
#source <(sudo cat /etc/bash.bashrc) Issue running this command with calm.  Can run this command from putty
#source ~/.bashrc
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# install Node JS version 22.3
nvm install 22
node -v
npm -v
