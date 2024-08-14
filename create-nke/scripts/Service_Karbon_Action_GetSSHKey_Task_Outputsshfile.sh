echo "
#!/bin/sh
private_key='@@{decoded_private_key}@@'
user_cert='@@{certificate}@@'
tag=KARBON
cluster_uuid=@@{nke_cluster_uuid}@@

save_cert=false
file_copy=false

# Initialising the private key file path
if [ -z '@@{nke_cluster_uuid}@@' ]; then
    private_key_file=/tmp/KARBON_user
else
    private_key_file=/tmp/KARBON_user_@@{nke_cluster_uuid}@@
fi

# Initialising the cert file path
if [ -z '@@{nke_cluster_uuid}@@' ]; then
    cert_file=/tmp/KARBON_user-cert.pub
else
    cert_file=/tmp/KARBON_user_@@{nke_cluster_uuid}@@-cert.pub
fi

while getopts ':cs' opt; do
  case $opt in
    c)
      file_copy=true
      ;;
    s)
      save_cert=true
      echo 'Private Key File: @@{decoded_private_key}@@'
      echo 'User Cert File: @@{certificate}@@'
      ;;
    \?)
      echo 'Invalid option: -$OPTARG' >&2
      exit 1
      ;;
  esac
done

# For parsing non-option arguments
shift $((OPTIND-1))

# Creating Private Key file
rm -f $private_key_file
printf '%b' '$private_key' > $private_key_file
chmod 0400 $private_key_file

# Creating Cert file
rm -f $cert_file
printf '%b' '$user_cert' > $cert_file
chmod 0400 $cert_file

if [ $# -eq 0 ]; then
  if $save_cert; then
    exit 0
  else
    read -p 'Enter KARBON VM IP: ' vm_ip
  fi
else
  vm_ip=$1
  shift
  if $file_copy; then
    src=$1
    dst=$2
  else
    cmd=$@
  fi
fi

echo '================== $vm_ip =================='
if $file_copy; then
  scp -i $private_key_file -oPubkeyAcceptedKeyTypes=ssh-ed25519-cert-v01@openssh.com $src 'nutanix@$vm_ip:$dst'
else
  ssh -i $private_key_file 'nutanix@$vm_ip' -oPubkeyAcceptedKeyTypes=ssh-ed25519-cert-v01@openssh.com '$cmd'
fi

if [ $save_cert = false ]; then
  rm -f $private_key_file
  rm -f $cert_file
fi " | tee /home/nutanix/@@{cluster_name}@@-ssh.sh
sudo chmod +x /home/nutanix/@@{cluster_name}@@-ssh.sh
