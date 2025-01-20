#sudo yum install -y java-1.8.0-openjdk-devel
#sudo java -version

sudo dnf -y install unzip vim wget net-tools
echo "Removing Java"
sudo rpm -qa | grep openjdk | sudo xargs dnf -y remove
echo "Installing JDK 17"
sudo dnf install -y java-17-openjdk java-17-openjdk-devel