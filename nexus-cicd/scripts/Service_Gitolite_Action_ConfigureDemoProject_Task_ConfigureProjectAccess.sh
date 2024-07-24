
echo "Create Key File"
echo @@{jenkins_public_key}@@ >> ~/gitolite-admin/keydir/jenkins.pub 
cp /tmp/git.pub ~/gitolite-admin/keydir/git.pub 

echo "Configure @@{initial_project_name}@@ Repository Access"
echo "repo @@{initial_project_name}@@" >> ~/gitolite-admin/conf/gitolite.conf
echo "    RW+     =   @all" >> ~/gitolite-admin/conf/gitolite.conf 
echo "    RW+     =   @@{Nutanix Key.username}@@" >> ~/gitolite-admin/conf/gitolite.conf 
echo "    R       =   jenkins" >> ~/gitolite-admin/conf/gitolite.conf
echo "    R       =   git" >> ~/gitolite-admin/conf/gitolite.conf

#echo "Cloning the gitolite-admin repository using nutanix user"
#git clone nutanix@@@{address}@@:gitolite-admin.git
echo "Check IN and Commit Changes"
cd gitolite-admin
git config --global user.name nutanix
git config --global user.email nutanix@@@{domain_name}@@
git config --global push.default matching
git add keydir/jenkins.pub
git add keydir/git.pub
git add conf/gitolite.conf
git commit -m "Added Jenkins"
git push origin master
