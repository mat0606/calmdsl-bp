
sudo dnf -y update
sudo dnf -y install samba-common-tools realmd oddjob oddjob-mkhomedir sssd adcli krb5-workstation
# https://docs.rockylinux.org/guides/security/authentication/active_directory_authentication/
#sudo dnf -y install realmd oddjob oddjob-mkhomedir sssd adcli krb5-workstation