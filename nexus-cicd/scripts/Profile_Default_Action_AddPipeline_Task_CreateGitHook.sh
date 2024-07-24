echo 'StrictHostKeyChecking no' > ~/.ssh/config
echo "Create Hook"
ssh @@{Gitolite.address}@@ 'printf "#!/bin/bash\n/usr/bin/curl --user admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080/job/@@{new_project_name}@@/buildWithParameters?token=ThisIsTheAPITokenToUse\n" | sudo su -c "tee ~/repositories/@@{new_project_name}@@.git/hooks/post-receive" - git'
ssh @@{Gitolite.address}@@ 'sudo su -c "chmod 775 ~/repositories/@@{new_project_name}@@.git/hooks/post-receive" - git'
echo "Complete Hook"