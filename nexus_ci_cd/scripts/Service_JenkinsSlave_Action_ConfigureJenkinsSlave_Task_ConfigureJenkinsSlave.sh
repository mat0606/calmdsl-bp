JENKINS_URL=http://@@{Jenkins Master.address}@@:8080
NODE_NAME=@@{name}@@
NODE_IP=@@{address}@@
NODE_SLAVE_HOME='/home/nutanix'
EXECUTORS=1
SSH_PORT=22
CRED_ID=Jenkins-Slave
LABELS=build
USERID=admin

echo "Creating credential"
echo '<com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>
  <scope>GLOBAL</scope>
  <id>Jenkins-Slave</id>
  <description>Slave Login</description>
  <username>@@{Ubuntu Credential.username}@@</username>
  <password>@@{Ubuntu Credential.secret}@@</password>
</com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl>' | sudo java -jar /home/nutanix/jenkins-cli.jar -auth admin:@@{Jenkins Master.jenkins_authorization}@@ -s http://@@{Jenkins Master.address}@@:8080  create-credentials-by-xml system::system::jenkins _ 

echo "Creating slave node"
cat <<EOF | sudo java -jar ${NODE_SLAVE_HOME}/jenkins-cli.jar -auth admin:@@{Jenkins Master.jenkins_authorization}@@ -s ${JENKINS_URL} create-node ${NODE_NAME}
<slave>
  <name>${NODE_NAME}</name>
  <description>Jenkins Slave Node</description>
  <remoteFS>${NODE_SLAVE_HOME}</remoteFS>
  <numExecutors>${EXECUTORS}</numExecutors>
  <mode>NORMAL</mode>
  <launcher class="hudson.plugins.sshslaves.SSHLauncher" plugin="ssh-slaves">
    <host>${NODE_IP}</host>
    <port>${SSH_PORT}</port>
    <credentialsId>${CRED_ID}</credentialsId>
    <maxNumRetries>0</maxNumRetries>
    <retryWaitTime>0</retryWaitTime>
    <sshHostKeyVerificationStrategy class="hudson.plugins.sshslaves.verifiers.NonVerifyingKeyVerificationStrategy"/>
  </launcher>
  <label>${LABELS}</label>
  <nodeProperties/>
</slave>
EOF