cp /etc/fstab /etc/fstab.orig
echo "/dev/sdb /var/www/html xfs defaults 2 0" | tee /etc/fstab