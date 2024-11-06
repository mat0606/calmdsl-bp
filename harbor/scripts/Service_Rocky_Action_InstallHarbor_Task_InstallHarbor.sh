cd harbor
cp harbor.yml.tmpl harbor.yml
sed -i "s|/your/certificate/path|/etc/pki/tls/certs/harbor_registry.crt|g" harbor.yml
sed -i "s|/your/private/key/path|/etc/pki/tls/certs/harbor_registry.key|g" harbor.yml
sed -i "s|reg.mydomain.com|@@{name}@@.@@{domain_name}@@|g" harbor.yml
sudo ./prepare
sudo ./install.sh --with-trivy 