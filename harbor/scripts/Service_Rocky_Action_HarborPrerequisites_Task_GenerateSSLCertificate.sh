sudo mkdir -p /etc/pki/tls/certs
cd /etc/pki/tls/certs

echo "
[ ca ]
# X509 extensions for a ca
keyUsage                = critical, cRLSign, keyCertSign
basicConstraints        = CA:TRUE, pathlen:0
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid:always,issuer:always

[ server ]
# X509 extensions for a server
keyUsage                = critical,digitalSignature,keyEncipherment
extendedKeyUsage        = serverAuth,clientAuth
basicConstraints        = critical,CA:FALSE
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid,issuer:always
" | sudo tee x509.ext


echo "
[ req ]
default_bits			= 4096
default_md         		= sha512
distinguished_name 		= req_distinguished_name
req_extensions   		= req_ext
prompt 					= no


[ req_distinguished_name ]
countryName     			= 'SG'
stateOrProvinceName 		= 'Singapore'
localityName    			= 'Singapore'
organizationName  			= 'Sales'
commonName     				= 'rootCA.@@{domain_name}@@'

[ req_ext ]
subjectAltName = @alt_names
[alt_names]
DNS.1  = rootCA.@@{domain_name}@@
" | sudo tee rootCA.cnf

echo "Generate key for rootCA"
sudo openssl req -out rootCA.csr -newkey rsa:4096 --sha512 -nodes -keyout rootCA.key -config rootCA.cnf
echo "Generate rootCA cert"
sudo openssl x509 -req -sha256 -extfile x509.ext -extensions ca -in rootCA.csr -signkey rootCA.key -days 1095 -out rootCA.crt

echo "
[ req ]  
default_bits       = 4096
default_md         = sha512
default_keyfile    = harbor_registry.key
prompt             = no
encrypt_key        = no
distinguished_name = req_distinguished_name
req_extensions     = req_ext

# distinguished_name
[ req_distinguished_name ]  
countryName            = 'SG' 
localityName           = 'Singapore'
stateOrProvinceName    = 'Singapore'
organizationName       = 'Sales'
commonName             = '@@{name}@@.@@{domain_name}@@'

[ req_ext ]
subjectAltName = @alt_names
[alt_names]
DNS.1  = @@{name}@@.@@{domain_name}@@
" | sudo tee harbor_certs.cnf

echo "Generate Harbor CSR"
sudo openssl req -out harbor_registry.csr -newkey rsa:4096 --sha512 -nodes -keyout harbor_registry.key -config harbor_certs.cnf

echo "Create Self Signed Certificate"
#sudo openssl x509 -in harbor_registry.csr -out harbor_registry.crt -req -signkey harbor_registry.key -days 3650

export harborSAN=$(openssl req -noout -text -in harbor_registry.csr | grep DNS)
echo "subjectAltName = " $harborSAN | sudo tee harbortext

echo "Create Harbor Certificate and signed with rootCA cert"
sudo openssl x509 -req -in harbor_registry.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out harbor_registry.crt -days 1024 -sha256 -extfile harbortext

