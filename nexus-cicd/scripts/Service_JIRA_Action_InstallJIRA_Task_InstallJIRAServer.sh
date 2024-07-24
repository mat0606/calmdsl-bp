sudo yum -y install wget
cd /opt
sudo wget https://www.atlassian.com/software/jira/downloads/binary/@@{jira_binary}@@.bin
sudo chmod +x @@{jira_binary}@@.bin

echo "
rmiPort$Long=8005
app.jiraHome=/opt/atlassian/jira-home
app.confHome=/var/atlassian/jire-home/conf
app.install.service$Boolean=true
sys.adminRights$Boolean=true
sys.confirmedUpdateInstallationString=false
sys.languageId=en
sys.installationDir=/opt/atlassian/jira
executeLauncherAction$Boolean=true
httpPort$Long=8080
portChoice=default" | sudo tee /opt/response.varfile

sudo ./@@{jira_binary}@@.bin -q -varfile /opt/response.varfile