export NEXUS_HOME=/opt/nexus
sudo rm -rf $NEXUS_HOME/bin/nexus.vmoptions

echo "-Xms4096m
-Xmx4096m
-XX:MaxDirectMemorySize=4096m
-XX:+UnlockDiagnosticVMOptions
-XX:+LogVMOutput
-XX:LogFile=../sonatype-work/nexus3/log/jvm.log
-XX:-OmitStackTraceInFastThrow
-Djava.net.preferIPv4Stack=true
-Dkaraf.home=.
-Dkaraf.base=.
-Dkaraf.etc=etc/karaf
-Djava.util.logging.config.file=etc/karaf/java.util.logging.properties
-Dkaraf.data=../sonatype-work/nexus3
-Dkaraf.log=../sonatype-work/nexus3/log
-Djava.io.tmpdir=../sonatype-work/nexus3/tmp
-Dkaraf.startLocalConsole=false
-Djdk.tls.ephemeralDHKeySize=2048
# -Djava.endorsed.dirs=lib/endorsed
#
# additional vmoptions needed for Java9+
#
--add-reads=java.xml=java.logging
--add-exports=java.base/org.apache.karaf.specs.locator=java.xml,ALL-UNNAMED
--patch-module
java.base=./lib/endorsed/org.apache.karaf.specs.locator-4.3.9.jar
--patch-module
java.xml=./lib/endorsed/org.apache.karaf.specs.java.xml-4.3.9.jar
--add-opens
java.base/java.security=ALL-UNNAMED
--add-opens
java.base/java.net=ALL-UNNAMED
--add-opens
java.base/java.lang=ALL-UNNAMED
--add-opens
java.base/java.util=ALL-UNNAMED
--add-opens
java.naming/javax.naming.spi=ALL-UNNAMED
--add-opens
java.rmi/sun.rmi.transport.tcp=ALL-UNNAMED
--add-exports=java.base/sun.net.www.protocol.http=ALL-UNNAMED
--add-exports=java.base/sun.net.www.protocol.https=ALL-UNNAMED
--add-exports=java.base/sun.net.www.protocol.jar=ALL-UNNAMED
--add-exports=jdk.xml.dom/org.w3c.dom.html=ALL-UNNAMED
--add-exports=jdk.naming.rmi/com.sun.jndi.url.rmi=ALL-UNNAMED
--add-exports=java.security.sasl/com.sun.security.sasl=ALL-UNNAMED
--add-exports=java.base/sun.security.x509=ALL-UNNAMED
--add-exports=java.base/sun.security.rsa=ALL-UNNAMED
--add-exports=java.base/sun.security.pkcs=ALL-UNNAMED
" | sudo tee $NEXUS_HOME/bin/nexus.vmoptions

sudo chown -R nexus:nexus $NEXUS_HOME/bin