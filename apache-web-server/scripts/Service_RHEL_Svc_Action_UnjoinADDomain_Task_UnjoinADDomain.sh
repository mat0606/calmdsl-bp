password=@@{Domain Administrator.secret}@@
export password

echo "Leaving Active Directory Domain"
sudo realm leave --verbose
sudo realm list