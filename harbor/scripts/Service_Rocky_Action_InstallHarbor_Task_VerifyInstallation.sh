#sudo docker compose ps
#sudo docker login @@{name}@@.@@{domain_name}@@:443/registry -u @@{Harbor.username}@@ -p @@{Harbor.secret}@@

echo "@@{Harbor.secret}@@" | sudo docker login @@{name}@@.@@{domain_name}@@:443/registry -u @@{Harbor.username}@@ --password-stdin