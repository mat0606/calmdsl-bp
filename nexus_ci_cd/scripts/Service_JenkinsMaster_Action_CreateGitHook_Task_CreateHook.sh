echo 'StrictHostKeyChecking no' > ~/.ssh/config
echo "Create Hook in Workstation"
ssh @@{Gitolite.address}@@ 'pwd'
ssh @@{Gitolite.address}@@ 'printf "/usr/bin/curl --user admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080/job/@@{initial_project_name}@@/buildWithParameters?token=ThisIsTheAPITokenToUse\n" | sudo su -c "tee ~/repositories/@@{initial_project_name}@@.git/hooks/post-receive" - git'
ssh @@{Gitolite.address}@@ 'sudo su -c "chmod 775 ~/repositories/@@{initial_project_name}@@.git/hooks/post-receive" - git'
echo "Complete Hook in Workstatation"