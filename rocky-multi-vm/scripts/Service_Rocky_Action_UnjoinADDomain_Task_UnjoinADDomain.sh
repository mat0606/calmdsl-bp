password=@@{Domain Administrator.secret}@@
export password

echo "Leaving Active Directory Domain"
#sudo echo $password | sudo realm leave -U @@{Domain Administrator.username}@@ @@{domain_name}@@ --verbose
#sudo echo $password | sudo realm leave @@{Domain_Server}@@.@@{domain_name}@@
sudo realm leave @@{Domain_Server}@@.@@{domain_name}@@
sudo realm list