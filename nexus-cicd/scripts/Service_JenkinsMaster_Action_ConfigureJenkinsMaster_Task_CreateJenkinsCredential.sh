echo 'Wait for Jenkins Instance Restart'
sleep 60

echo 'Create Jenkins Credential'
JENKINS_SSH_KEY=$(sudo cat /var/lib/jenkins/.ssh/id_rsa)

echo '<com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey plugin="ssh-credentials@1.13">
  <scope>GLOBAL</scope>
  <id>Jenkins</id>
  <description></description>
  <username>jenkins</username>
  <privateKeySource class="com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource">
    <privateKey>@@{Nutanix Key.secret}@@</privateKey>
  </privateKeySource>
</com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey>' | sudo java -jar jenkins-cli.jar -auth admin:@@{jenkins_authorization}@@ -s http://@@{address}@@:8080 create-credentials-by-xml system::system::jenkins _
