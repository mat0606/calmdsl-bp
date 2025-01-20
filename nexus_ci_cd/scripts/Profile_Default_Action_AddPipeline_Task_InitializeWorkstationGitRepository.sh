echo "Initialize DevOps Git Project"
git clone git@@@{Gitolite.name}@@.@@{domain_name}@@:@@{new_project_name}@@.git

cd @@{new_project_name}@@

git config user.name nutanix
git config user.email nutanix@@@{name}@@.@@{domain_name}@@
git config --global push.default matching
