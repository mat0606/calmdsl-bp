echo "Get the MySQL 8.0 installer"

#sudo wget https://repo.mysql.com/@@{mysql_binary}@@
sudo wget https://dev.mysql.com/get/Downloads/MySQL-8.0/@@{mysql_binary}@@
sudo tar -xvf @@{mysql_binary}@@

echo "Install it in the local yum repository"

sudo yum -y localinstall @@{mysql_binary}@@

echo "Verify it in the yum repository"

sudo yum repolist enabled | grep "mysql.*-community.*"

echo "Installing MySQL Server"

sudo yum -y install mysql-community-server

echo "Starting MySQL service"

sudo service mysqld start
sudo service mysqld status

echo "Retrieving MySQL Temporary Password"

tmpPasswd="$(sudo grep 'temporary password' /var/log/mysqld.log | awk -F ":" '{print $4}')"
#sudo export tmpPasswd
sudo echo "Temp SQL password: " $tmpPasswd
#"mysql_password=$tmpPasswd"

echo "Logging into MySQL database"

sudo yum install -y expect

MYSQL_UPDATE=$(expect -c "
set timeout 5
spawn mysql -u root -p
expect \"Enter password: \"
send \"${tmpPasswd}\r\"
expect \"mysql>\"
send \"ALTER USER 'root'@'localhost' IDENTIFIED BY 'nutanix/4u';\r\"
expect \"mysql>\"
send \"CREATE DATABASE jiradb CHARACTER SET utf8 COLLATE utf8_bin;\r\"
expect \"mysql>\"
send \"grant all privileges on jiradb.* to 'jira'@'%' identified by 'syslint123!@#';\r\"
expect \"mysql>\"
send \"flush privileges;\r\"
expect \"mysql>\"
send \"quit;\r\"
expect eof
")

echo "$MYSQL_UPDATE"

# remove expect program
sudo yum remove -y expect

echo "Downloading the MySQL Connector"

cd /opt
sudo wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.35.tar.gz
sudo tar -zxvf mysql-connector-java-5.1.35.tar.gz
cd /opt/mysql-connector-java-5.1.35
sudo cp mysql-connector-java-5.1.35-bin.jar /opt/atlassian/jira/lib/
