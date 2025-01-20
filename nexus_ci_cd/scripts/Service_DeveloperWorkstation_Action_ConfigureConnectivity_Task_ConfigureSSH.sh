echo "The ssh key is setup in the disk image.  This task is not necessary"

#mkdir ~/.ssh
#chmod 700 ~/.ssh
# Due to a bug in Calm 3.5.0, I was unable to use the credential macro to output the private key in the correct format
#echo @@{Nutanix Key.secret}@@ > ~/.ssh/id_rsa

#echo "@@{Nutanix Key.secret}@@" | tee ~/.ssh/id_rsa

#chmod 600 ~/.ssh/id_rsa
#echo @@{nutanix_public_key}@@ > ~/.ssh/id_rsa.pub
#chmod 600 ~/.ssh/id_rsa.pub