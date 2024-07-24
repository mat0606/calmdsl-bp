echo "Configure @@{new_project_name}@@ Repository Access"
echo "repo @@{new_project_name}@@" >> ~/gitolite-admin/conf/gitolite.conf
echo "    RW+     =   @all" >> ~/gitolite-admin/conf/gitolite.conf 
echo "    R       =   jenkins" >> ~/gitolite-admin/conf/gitolite.conf 

echo "Check IN and Commit Changes"
cd gitolite-admin
git add conf/gitolite.conf
git commit -m "Added @@{new_project_name}@@ Repository"
git push origin master