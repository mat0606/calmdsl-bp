#sudo apt-get install default-jre -y
apt-cache search openjdk | grep openjdk-17
echo "Installing OpenJDK 17"
sudo apt install -y openjdk-17-jdk
echo "Installing OpenJRE 17"
sudo apt install -y openjdk-17-jre
java --version