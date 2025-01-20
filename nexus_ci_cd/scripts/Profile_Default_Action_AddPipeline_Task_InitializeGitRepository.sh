echo "Create and Configure @@{new_project_name}@@ Repository"
sudo su -c 'mkdir ~/repositories/@@{new_project_name}@@.git' - git
sudo su -c 'cd ~/repositories/@@{new_project_name}@@.git && git init --bare' - git
