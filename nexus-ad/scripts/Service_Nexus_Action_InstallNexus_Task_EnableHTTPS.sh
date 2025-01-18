echo "Enable HTTPS"
cd /opt/nexus/etc
sudo mv nexus-default.properties nexus-default.properties.bak

echo '
# Jetty section
application-port=8081
application-port-ssl=8443
application-host=@@{address}@@
nexus-args=${jetty.etc}/jetty.xml,${jetty.etc}/jetty-http.xml,${jetty.etc}/jetty-https.xml,${jetty.etc}/jetty-requestlog.xml
nexus-context-path=/
ssl.etc=/opt/nexus/etc/ssl

# Nexus section
nexus-edition=nexus-pro-edition
nexus-features=\
nexus-pro-feature

# nexus.hazelcast.discovery.isEnabled=true
' | sudo tee -a nexus-default.properties

sudo chown nexus:nexus nexus-default.properties 

# Mask off the following line because Nexus Repository ManagerOSS 3.62.0-01 application-port-ssl is no longer in use
#cd /opt/nexus/etc/jetty
#sudo mv jetty-https.xml jetty-https.xml.bak
#sudo wget https://matthewnutanixpublic.s3.us-east-2.amazonaws.com/Nexus/jetty/jetty-https.xml
#sudo chown nexus:nexus jetty-https.xml

#sudo systemctl restart nexus.service



