export NEXUS_HOME=/opt/nexus
sudo rm -rf $NEXUS_HOME/bin/nexus.vmoptions

echo "-Xms4096M
-Xmx4096M 
-XX:MaxDirectMemorySize=4G
-XX:+UnlockDiagnosticVMOptions
-XX:+UnsyncloadClass
-XX:+LogVMOutput
-XX:LogFile=/Data/nexus-data/nexus3/log/jvm.log
-Djava.net.preferIPv4Stack=true
-Dkaraf.home=.
-Dkaraf.base=.
-Dkaraf.etc=etc/karaf
-Djava.util.logging.config.file=etc/karaf/java.util.logging.properties
-Dkaraf.data=/Data/nexus-data/nexus3
-Djava.io.tmpdir=/Data/nexus-data/nexus3/tmp
-Dkaraf.startLocalConsole=false

#
# additional vmoptions needed for Java9+
#
# --add-reads=java.xml=java.logging
# --add-exports=java.base/org.apache.karaf.specs.locator=java.xml,ALL-UNNAMED
# --patch-module=java.base=lib/endorsed/org.apache.karaf.specs.locator-4.2.9.jar
# --patch-module=java.xml=lib/endorsed/org.apache.karaf.specs.java.xml-4.2.9.jar
# --add-opens=java.base/java.security=ALL-UNNAMED
# --add-opens=java.base/java.net=ALL-UNNAMED
# --add-opens=java.base/java.lang=ALL-UNNAMED
# --add-opens=java.base/java.util=ALL-UNNAMED
# --add-opens=java.naming/javax.naming.spi=ALL-UNNAMED
# --add-opens=java.rmi/sun.rmi.transport.tcp=ALL-UNNAMED
# --add-exports=java.base/sun.net.www.protocol.http=ALL-UNNAMED
# --add-exports=java.base/sun.net.www.protocol.https=ALL-UNNAMED
# --add-exports=java.base/sun.net.www.protocol.jar=ALL-UNNAMED
# --add-exports=jdk.xml.dom/org.w3c.dom.html=ALL-UNNAMED
# --add-exports=jdk.naming.rmi/com.sun.jndi.url.rmi=ALL-UNNAMED
#
# comment out this vmoption when using Java9+
#
-Djava.endorsed.dirs=lib/endorsed" | sudo tee $NEXUS_HOME/bin/nexus.vmoptions

sudo chown -R nexus:nexus $NEXUS_HOME/bin