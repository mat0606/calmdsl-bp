echo "@@{ROCKY.secret}@@" | tee ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
echo "@@{ROCKY.public_key}@@" | tee ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/authorized_keys

rm ~/.ssh/karbon_id_rsa.pub
echo "@@{certificate}@@" | tee ~/.ssh/karbon_id_rsa.pub
rm ~/.ssh/karbon_id_rsa
#echo "@@{private_key}@@" | tee /home/centos/.ssh/karbon_id_rsa
echo "@@{karbon_ssh}@@" | tee /home/nutanix/.ssh/karbon_id_rsa
echo "@@{private_key}@@"