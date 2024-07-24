cd /usr/src
#wget https://ftp.openssl.org/source/@@{openssl_version}@@.tar.gz --no-check-certificate
# changed to this url on 4 Jun 24
wget https://www.openssl.org/source/@@{openssl_version}@@.tar.gz --no-check-certificate
tar -zxvf @@{openssl_version}@@.tar.gz