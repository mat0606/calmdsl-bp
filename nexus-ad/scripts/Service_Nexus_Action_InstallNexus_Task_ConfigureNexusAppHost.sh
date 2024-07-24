export NEXUS_HOME=/opt/nexus

sudo sed -i 's/0.0.0.0/@@{address}@@/g' $NEXUS_HOME/etc/nexus-default.properties

echo "nexus - nofile 65536" | sudo tee /etc/security/limits.conf