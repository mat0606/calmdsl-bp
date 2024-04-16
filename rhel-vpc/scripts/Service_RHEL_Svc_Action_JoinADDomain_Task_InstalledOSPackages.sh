
#sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
#sudo yum-config-manager --add-repo=http://mirror.centos.org/centos-7/7.9.2009/extras/x86_64
sudo dnf -y update
#sudo dnf -y install realmd libnss-sss libpam-sss sssd sssd-tools adcli samba-common samba-common-bin samba-common-tools oddjob oddjob-mkhomedir packagekit 
# Refer to https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/integrating_rhel_systems_directly_with_windows_active_directory/index#discovering-and-joining-an-ad-domain-using-sssd_connecting-directly-to-ad
sudo dnf -y install samba-common-tools realmd oddjob oddjob-mkhomedir sssd adcli krb5-workstation