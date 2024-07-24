set -x
sudo apt install -y git
echo "Initialize @@{initial_project_name}@@ Git Project"
git clone git@@@{Gitolite.name}@@.@@{domain_name}@@:@@{initial_project_name}@@.git

cd @@{initial_project_name}@@

git config user.name nutanix
git config user.email nutanix@@@{name}@@.@@{domain_name}@@
git config --global push.default matching
