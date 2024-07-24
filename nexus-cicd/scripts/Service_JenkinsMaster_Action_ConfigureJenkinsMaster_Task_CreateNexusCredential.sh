echo "Creating Nexus User credential"
echo '<com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
  <scope>GLOBAL</scope>
  <id>nexus-user-credentials</id>
  <description>Login Details to Nexus Repository Manager</description>
  <username>@@{Nexus Jenkins Credential.username}@@</username>
  <password>@@{Nexus Jenkins Credential.secret}@@</password>
</com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>' | sudo java -jar /home/nutanix/jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 create-credentials-by-xml system::system::jenkins _ 
