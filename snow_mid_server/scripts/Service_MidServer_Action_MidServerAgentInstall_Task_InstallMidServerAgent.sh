#!/bin/bash

set -ex

ZIP_FILE_NAME=$(echo "@@{midserver_agent_url}@@" | xargs -d / -n1 | tail -2)
SERVICENOW_PASS=$(sudo sed 's:/:\\/:g' <<< "@@{snow_mid_pwd}@@")

#for troubleshooting purpose
echo $SERVICENOW_PASS | sudo tee snowpass.txt

# create midesrver agent dir and set permissions
sudo mkdir -p /servicenow/@@{snow_instance_name}@@/agent
# download, unzip and move midserver agent
sudo wget "@@{midserver_agent_url}@@"
sudo unzip "${ZIP_FILE_NAME}"
sudo mv agent /servicenow/@@{snow_instance_name}@@/

# sed update config.xml
#sudo sed -i -e "s/YOUR_INSTANCE.service-now.com/@@{snow_instance_name}@@.service-now.com/" /servicenow/@@{snow_instance_name}@@/agent/config.xml
#sudo sed -i -e "s/YOUR_INSTANCE_USER_NAME_HERE/@@{snow_mid_user}@@/" /servicenow/@@{snow_instance_name}@@/agent/config.xml
# Remove and add back the line
#sudo sed -i '/mid.instance.password/d' /servicenow/@@{snow_instance_name}@@/agent/config.xml
#sudo sed -i '30i <parameter name="mid.instance.password" secure="true" value="@@{snow_mid_pwd}@@"/>' /servicenow/@@{snow_instance_name}@@/agent/config.xml

#sudo sed -i -e "s/ENCv2/${SERVICENOW_PASS}/" /servicenow/@@{snow_instance_name}@@/agent/config.xml
#sudo sed -i -e "s/YOUR_MIDSERVER_NAME_GOES_HERE/@@{snow_instance_name}@@/" /servicenow/@@{snow_instance_name}@@/agent/config.xml

#cd /
#sudo chown -R @@{RHEL.username}@@:@@{RHEL.username}@@ /servicenow/

# start and install services
#echo "yes" | sudo /servicenow/@@{snow_instance_name}@@/agent/bin/mid.sh installstart
#sudo systemctl status mid.service
