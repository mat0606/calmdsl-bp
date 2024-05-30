sudo chronyc sources
sudo systemctl stop chronyd
#sudo chronyd -q "server @@{Domain_Server}@@.@@{domain_name}@@ iburst"
sudo systemctl start chronyd
# systemctl status chronyd
sudo chronyc tracking
