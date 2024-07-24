# Setting up the default JDK
alternatives --config java 

# Setting up JAVA_HOME and NEXUS_HOME
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.262.b10-0.el7_8.x86_64
export NEXUS_HOME=/opt/nexus
source /etc/bashrc

# Check the JAVA version
java -version