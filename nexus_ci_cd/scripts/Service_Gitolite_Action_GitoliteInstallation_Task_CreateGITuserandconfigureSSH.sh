sudo adduser --system --shell /bin/bash --group --disabled-password --home /home/git git

sudo su -c 'mkdir ~/bin; chmod 750 ~/bin' - git
sudo su -c 'echo "PATH=$PATH:~/bin" >> ~/.profile' - git

echo "Installing OpenSSL"
sudo apt install -y openssl
pass=@@{Ubuntu Credential.secret}@@
echo $pass
echo "Modify the password for GIT user" 
sudo usermod --password $(openssl passwd -1 "$pass") git
echo "Creating the ssh directory and configuring ssh key"
echo "@@{Gitolite Key.secret}@@" | tee /tmp/git.key
echo "@@{git_public_key}@@" | tee /tmp/git.pub
chmod 644 /tmp/git.pub
chmod 644 /tmp/git.key
sudo su -c 'mkdir -p /home/git/.ssh' - git
sudo su -c 'chmod 700 /home/git/.ssh' - git
sudo su -c 'cp /tmp/git.pub /home/git/.ssh/id_rsa.pub' - git
sudo su -c 'cp /tmp/git.key /home/git/.ssh/id_rsa' - git
sudo su -c 'cp /home/git/.ssh/id_rsa.pub /home/git/.ssh/authorized_keys' - git
sudo su -c 'chmod 600 /home/git/.ssh/authorized_keys' - git
sudo su -c 'chmod 600 /home/git/.ssh/id_rsa*' - git
#sudo su -c 'ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<<y >/dev/null 2>&1' - git
sudo su -c 'echo "set -o vi" >> ~/.bashrc' - git
sudo su -c 'echo "StrictHostKeyChecking no" > ~/.ssh/config' - git
