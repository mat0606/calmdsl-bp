echo 'Update Jenkins Configuration'
sudo su -c "sed -i 's/<installStateName>NEW</<installStateName>RUNNING</' ~/config.xml" - jenkins
sudo su -c "sed -i 's/numExecutors>2</numExecutors>0</' ~/config.xml" - jenkins

echo 'Create Location Configuration'
printf "<?xml version='1.1' encoding='UTF-8'?>
<jenkins.model.JenkinsLocationConfiguration>
  <jenkinsUrl>http://@@{address}@@:8080/</jenkinsUrl>
</jenkins.model.JenkinsLocationConfiguration>" | sudo su -c 'tee ~/jenkins.model.JenkinsLocationConfiguration.xml' - jenkins

echo 'Set State and Version Configurations'
sudo cat /var/lib/jenkins.install.UpgradeWizard.state | sudo su -c 'tee ~/jenkins.install.InstallUtil.lastExecVersion' - jenkins

echo 'Configure SSH'
printf "<?xml version='1.1' encoding='UTF-8'?>
<org.jenkinsci.main.modules.sshd.SSHD>
  <port>22</port>
</org.jenkinsci.main.modules.sshd.SSHD>" | sudo su -c 'tee ~/org.jenkinsci.main.modules.sshd.SSHD.xml' - jenkins

echo 'Create @@{initial_project_name}@@ Pipeline'
sudo su -c 'mkdir -p ~/jobs/@@{initial_project_name}@@/builds' - jenkins
sudo su -c 'touch ~/jobs/@@{initial_project_name}@@/builds/legacyIds' - jenkins
sudo su -c 'echo 1 > ~/jobs/@@{initial_project_name}@@/nextBuildNumber' - jenkins

echo '<?xml version="1.1" encoding="UTF-8"?>
<flow-definition plugin="workflow-job@2.23">
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties>
    <hudson.model.ParametersDefinitionProperty>
      <parameterDefinitions>
        <hudson.model.StringParameterDefinition>
          <name>DOCKER_REGISTRY_USER</name>
          <description></description>
          <defaultValue>@@{Nexus Jenkins Credential.username}@@</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.PasswordParameterDefinition>
          <name>DOCKER_REGISTRY_PASSWORD</name>
          <description></description>
          <defaultValue>@@{Nexus Jenkins Credential.secret}@@</defaultValue>
        </hudson.model.PasswordParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>DOCKER_REGISTRY</name>
          <description></description>
          <defaultValue>@@{Nexus_vmname}@@.@@{domain_name}@@</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>DOCKER_PORT</name>
          <description></description>
          <defaultValue>@@{Nexus_Repo_Port}@@</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>REPO_NAME</name>
          <description></description>
          <defaultValue>@@{initial_project_name}@@</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
      </parameterDefinitions>
    </hudson.model.ParametersDefinitionProperty>
  </properties>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps@2.54">
     <scm class="hudson.plugins.git.GitSCM" plugin="git@3.9.1">
      <configVersion>2</configVersion>
      <userRemoteConfigs>
        <hudson.plugins.git.UserRemoteConfig>
          <url>git@@@{Gitolite.name}@@.@@{domain_name}@@:@@{initial_project_name}@@.git</url>
          <credentialsId>Jenkins</credentialsId>
        </hudson.plugins.git.UserRemoteConfig>
      </userRemoteConfigs>
      <branches>
        <hudson.plugins.git.BranchSpec>
          <name>*/master</name>
        </hudson.plugins.git.BranchSpec>
      </branches>
      <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
      <submoduleCfg class="list"/>
      <extensions/>
    </scm>
    <scriptPath>Jenkinsfile</scriptPath>
    <lightweight>true</lightweight>
  </definition>
  <triggers/>
  <authToken>ThisIsTheAPITokenToUse</authToken>
  <disabled>false</disabled>
</flow-definition>' | sudo su -c 'tee ~/jobs/@@{initial_project_name}@@/config.xml' - jenkins

sudo su -c 'chmod 644 ~/jobs/@@{initial_project_name}@@/config.xml' - jenkins
sudo su -c 'chmod 644 ~/jobs/@@{initial_project_name}@@/nextBuildNumber' - jenkins
sudo su -c 'chmod 644 ~/jobs/@@{initial_project_name}@@/builds/legacyIds' - jenkins

echo 'Setup Script Approvals'
echo '<?xml version="1.1" encoding="UTF-8"?>
<scriptApproval plugin="script-security@1.44">
  <approvedScriptHashes/>
  <approvedSignatures>
    <string>method groovy.json.JsonSlurperClassic parseText java.lang.String</string>
    <string>method java.util.Map remove java.lang.Object</string>
    <string>new groovy.json.JsonSlurperClassic</string>
    <string>new java.util.HashMap java.util.Map</string>
  </approvedSignatures>
  <aclApprovedSignatures/>
  <approvedClasspathEntries/>
  <pendingScripts/>
  <pendingSignatures/>
  <pendingClasspathEntries/>
</scriptApproval>' | sudo su -c 'tee ~/scriptApproval.xml' - jenkins

echo "Create @@{initial_project_name}@@ App Deploy Job"
sudo su -c 'mkdir -p ~/jobs/@@{initial_project_name}@@_deploy/builds' - jenkins
sudo su -c 'touch ~/jobs/@@{initial_project_name}@@_deploy/builds/legacyIds' - jenkins
sudo su -c 'echo 1 > ~/jobs/@@{initial_project_name}@@_deploy/nextBuildNumber' - jenkins
echo '<?xml version="1.1" encoding="UTF-8"?>
<flow-definition plugin="workflow-job@2.23">
  <actions/>
  <description></description>
  <keepDependencies>false</keepDependencies>
  <properties>
    <hudson.model.ParametersDefinitionProperty>
      <parameterDefinitions>
        <hudson.model.StringParameterDefinition>
          <name>NEXUS_IP</name>
          <description></description>
          <defaultValue>@@{Nexus_vmname}@@.@@{domain_name}@@</defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>REPO_NAME</name>
          <description></description>
          <defaultValue></defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
        <hudson.model.StringParameterDefinition>
          <name>BUILD_NUMBER</name>
          <description></description>
          <defaultValue></defaultValue>
          <trim>false</trim>
        </hudson.model.StringParameterDefinition>
      </parameterDefinitions>
    </hudson.model.ParametersDefinitionProperty>
  </properties>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition" plugin="workflow-cps@2.54">
    <script>import groovy.json.JsonSlurperClassic
import groovy.json.JsonOutput

node() {
    stage(&apos;Deploy Application Via Calm&apos;){
        echo &quot;Application deployment visual&quot;
    }
}

//def response = httpRequest authentication: &apos;PC-User&apos;, consoleLogResponseBody: false, customHeaders: [[maskValue: false, name: &apos;Content-Type&apos;, value: &apos;application/json&apos;]], ignoreSslErrors: true, responseHandle: &apos;LEAVE_OPEN&apos;, url: &apos;https://@@{pc_instance_ip}@@:9440/api/nutanix/v3/blueprints/@@{app_deploy_blueprint_uuid}@@&apos;
def response = httpRequest authentication: &apos;CalmVM-User&apos;, consoleLogResponseBody: false, customHeaders: [[maskValue: false, name: &apos;Content-Type&apos;, value: &apos;application/json&apos;]], ignoreSslErrors: true, responseHandle: &apos;LEAVE_OPEN&apos;, url: &apos;https://@@{CalmVM_IP}@@:9440/api/nutanix/v3/blueprints/@@{app_deploy_blueprint_uuid}@@&apos;

println(&quot;Status: &quot; + response.status)
//println(&quot;Content: &quot; + response.content)

def blueprint_spec = parseJSON(response.content)
def bp_index = 0
def var_index = 0
blueprint_spec.remove(&apos;status&apos;)
blueprint_spec[&apos;spec&apos;].remove(&apos;name&apos;)
blueprint_spec[&apos;spec&apos;][&apos;application_name&apos;] = REPO_NAME + &apos;@@{calm_random}@@Jenkins&apos; + BUILD_NUMBER.toString()
blueprint_spec[&apos;spec&apos;][&apos;app_profile_reference&apos;] = parseJSON(&apos;{&quot;kind&quot;: &quot;app_profile&quot;, &quot;uuid&quot;: &quot;@@{app_profile_uuid}@@&quot;}&apos;)
blueprint_spec[&apos;metadata&apos;][&apos;owner_reference&apos;] = parseJSON(&apos;{&quot;kind&quot;: &quot;user&quot;, &quot;uuid&quot;: &quot;00000000-0000-0000-0000-000000000000&quot;, &quot;name&quot;: &quot;admin&quot;}&apos;)
blueprint_spec[&apos;spec&apos;][&apos;resources&apos;][&apos;app_profile_list&apos;].each  { profileKey, profileRow -&gt; 
    println(&quot;Profile: ${profileKey}&quot;); 
    profileKey[&apos;variable_list&apos;].each { variableKey, variableRow -&gt;
        println(&quot;Variable: ${variableKey}&quot;); 
        if (variableKey[&apos;name&apos;] == &apos;build_number&apos;){
                blueprint_spec[&apos;spec&apos;][&apos;resources&apos;][&apos;app_profile_list&apos;][bp_index][&apos;variable_list&apos;][var_index][&apos;value&apos;] = BUILD_NUMBER.toString()
        } else if (variableKey[&apos;name&apos;] == &apos;project_name&apos;){
                blueprint_spec[&apos;spec&apos;][&apos;resources&apos;][&apos;app_profile_list&apos;][bp_index][&apos;variable_list&apos;][var_index][&apos;value&apos;] = REPO_NAME
        } else if (variableKey[&apos;name&apos;] == &apos;artifactory_ip&apos;){
                blueprint_spec[&apos;spec&apos;][&apos;resources&apos;][&apos;app_profile_list&apos;][bp_index][&apos;variable_list&apos;][var_index][&apos;value&apos;] = ARTIFACTORY_IP
        }
        var_index += 1;
    }; 
    bp_index += 1;
}
//println(&quot;Content: &quot; + blueprint_spec)

def payload = JsonOutput.toJson(blueprint_spec)
println(&quot;Payload: &quot; + payload)

// def result = httpRequest authentication: &apos;PC-User&apos;, consoleLogResponseBody: true, customHeaders: [[maskValue: false, name: &apos;Content-Type&apos;, value: &apos;application/json&apos;], [maskValue: false, name: &apos;Accept&apos;, value: &apos;application/json&apos;]], httpMode: &apos;POST&apos;, requestBody: payload, ignoreSslErrors: true, responseHandle: &apos;LEAVE_OPEN&apos;, url: &apos;https://@@{pc_instance_ip}@@:9440/api/nutanix/v3/blueprints/@@{app_deploy_blueprint_uuid}@@/launch&apos;
 def result = httpRequest authentication: &apos;CalmVM-User&apos;, consoleLogResponseBody: true, customHeaders: [[maskValue: false, name: &apos;Content-Type&apos;, value: &apos;application/json&apos;], [maskValue: false, name: &apos;Accept&apos;, value: &apos;application/json&apos;]], httpMode: &apos;POST&apos;, requestBody: payload, ignoreSslErrors: true, responseHandle: &apos;LEAVE_OPEN&apos;, url: &apos;https://@@{CalmVM_IP}@@:9440/api/nutanix/v3/blueprints/@@{app_deploy_blueprint_uuid}@@/launch&apos;
println(&quot;Status: &quot; + response.status)
println(&quot;Content: &quot; + response.content)

def parseJSON(json) {
    return new groovy.json.JsonSlurperClassic().parseText(json)
}
</script>
    <sandbox>true</sandbox>
  </definition>
  <triggers/>
  <disabled>false</disabled>
</flow-definition>'  | sudo su -c 'tee ~/jobs/@@{initial_project_name}@@_deploy/config.xml' - jenkins

sudo su -c 'chmod 644 ~/jobs/@@{initial_project_name}@@_deploy/config.xml' - jenkins
sudo su -c 'chmod 644 ~/jobs/@@{initial_project_name}@@_deploy/nextBuildNumber' - jenkins
sudo su -c 'chmod 644 ~/jobs/@@{initial_project_name}@@_deploy/builds/legacyIds' - jenkins

echo "@@{Nexus.address}@@ @@{Nexus_vmname}@@.@@{domain_name}@@ @@{Nexus_vmname}@@" | sudo tee -a /etc/hosts
#echo "@@{Docker Registry.address}@@ @@{Docker Registry.name}@@.@@{domain_name}@@ @@{Docker Registry.name}@@" | sudo tee -a /etc/hosts
echo "@@{Gitolite.address}@@ @@{Gitolite.name}@@.@@{domain_name}@@ @@{Gitolite.name}@@" | sudo tee -a /etc/hosts
#echo "@@{Artifactory.address}@@ artifactory.@@{domain_name}@@ artifactory" | sudo tee -a /etc/hosts
