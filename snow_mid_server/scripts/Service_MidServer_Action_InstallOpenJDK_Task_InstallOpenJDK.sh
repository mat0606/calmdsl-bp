sudo dnf remove -y javapackages-filesystem-0:6.0.0-4.el9.noarch
# ServiceNow Mid Server certified with JDK 11
# https://docs.servicenow.com/bundle/xanadu-servicenow-platform/page/product/mid-server/task/t_InstallAMIDServerOnLinux.html
sudo dnf install -y java-11-openjdk java-11-openjdk-devel