ldconfig
# Add in the link on 5 Jun 24 after masking off the prefix in the configure step
#ln -s /usr/src/@@{openssl_version}@@/bin/openssl /usr/bin/openssl
ln -s /usr/local/bin/openssl /usr/bin/openssl
tee /etc/profile.d/openssl.sh<<EOF
export PATH=/usr/bin:\$PATH
export LD_LIBRARY_PATH=/usr/lib:/usr/lib64:\$LD_LIBRARY_PATH
EOF
source /etc/profile.d/openssl.sh
