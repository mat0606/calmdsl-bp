# Creating necessory folder structure
sudo mkdir -p /Data/nexus-data /opt/nexus

# Download latest Nexus artifact
sudo wget -O /tmp/nexus.tar.gz http://download.sonatype.com/nexus/3/latest-unix.tar.gz

# Extract it to /opt/nexus
sudo tar xvfz /tmp/nexus.tar.gz -C /opt/nexus --strip-components 1

# Adding a service account for nexus
sudo useradd --system --no-create-home nexus

# Provide necessory folder permissions
sudo chown -R nexus:nexus /opt/nexus
sudo chown -R nexus:nexus /Data/nexus-data
