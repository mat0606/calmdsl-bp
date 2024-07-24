echo "Creating Prism Central User credential"
echo '<com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
  <scope>GLOBAL</scope>
  <id>PC-User</id>
  <description>Prism Central User</description>
  <username>@@{Prism Central User.username}@@</username>
  <password>@@{Prism Central User.secret}@@</password>
</com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>' | sudo java -jar /home/nutanix/jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 create-credentials-by-xml system::system::jenkins _ 
