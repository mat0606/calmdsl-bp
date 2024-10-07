curl -Lo @@{nkp_binary}@@ "@@{nkp_binary_download_url}@@/@@{nkp_binary}@@"
tar -zxvf @@{nkp_binary}@@
sudo mv nkp /usr/local/bin
nkp version