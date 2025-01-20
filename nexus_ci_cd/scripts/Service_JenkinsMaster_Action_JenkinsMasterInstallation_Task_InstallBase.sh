set -x

sudo add-apt-repository -y ppa:apt-fast/stable
sudo apt-get update
echo debconf apt-fast/maxdownloads string 16 | sudo debconf-set-selections
echo debconf apt-fast/dlflag boolean true | sudo debconf-set-selections
echo debconf apt-fast/aptmanager string apt-get | sudo debconf-set-selections
sudo apt-get install -y apt-fast
sudo apt-get install python2.7 -y
sudo apt-get install default-jre -y
sudo apt-get install curl -y 
sudo apt-get install make -y
sudo apt-get install wget -y
echo "alias python=python2.7" >> ~/.bashrc
sudo ln -s /usr/bin/python2.7 /usr/bin/python
