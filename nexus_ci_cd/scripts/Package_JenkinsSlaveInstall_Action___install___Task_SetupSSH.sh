mkdir ~/.ssh
chmod 700 ~/.ssh
echo 'StrictHostKeyChecking no' > ~/.ssh/config

echo "Create SSH Keys"
echo "@@{Nutanix Key.secret}@@" > ~/.ssh/id_rsa
echo "@@{nutanix_public_key}@@" > ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/id_rsa*
cp ~/.ssh/id_rsa.pub  ~/.ssh/authorized_keys

