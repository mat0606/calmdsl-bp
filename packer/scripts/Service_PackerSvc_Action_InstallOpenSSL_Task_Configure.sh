cd /usr/src
cd @@{openssl_version}@@
#./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic
./config --openssldir=/usr/src/@@{openssl_version}@@ --libdir=lib no-shared zlib-dynamic
make