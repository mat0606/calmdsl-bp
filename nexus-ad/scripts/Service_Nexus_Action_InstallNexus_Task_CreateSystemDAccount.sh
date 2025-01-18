export NEXUS_HOME=/opt/nexus
sudo rm -rf $NEXUS_HOME/bin/nexus.rc

echo "run_as_user=nexus" | sudo tee $NEXUS_HOME/bin/nexus.rc
sudo chown -R nexus:nexus $NEXUS_HOME/bin

sudo rm -rf /etc/systemd/system/nexus.service
echo "
[Unit]
Description=nexus service
After=network.target

[Service]
Type=forking
LimitNOFILE=65536
ExecStart=/opt/nexus/bin/nexus start
ExecStop=/opt/nexus/bin/nexus stop
User=nexus
Restart=on-abort

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/nexus.service

sudo chmod +x /etc/systemd/system/nexus.service

