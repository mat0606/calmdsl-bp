echo "Generate certificate"
keytool -genkeypair -keystore keystore.p12 -storepass password -alias jetty -keyalg RSA -keysize 2048 -validity 5000 -keypass nutanix/4u -dname 'CN=@@{name}@@.@@{domain_name}@@, OU=Sales, O=Nutanix, L=Unspecified, ST=Unspecified, C=SG' -storetype PKCS12 -ext san=dns:@@{name}@@.@@{domain_name}@@
echo "Extract nexus_server.pem"
openssl pkcs12 -nokeys -in keystore.p12 -out nexus_server.pem -passin pass:password
echo "Extract nexus_server.key"
openssl pkcs12 -nocerts -nodes -in keystore.p12 -out nexus_server.key -passin pass:password

sudo cp nexus_server.key /opt/nexus/etc/ssl
sudo cp nexus_server.pem /opt/nexus/etc/ssl
