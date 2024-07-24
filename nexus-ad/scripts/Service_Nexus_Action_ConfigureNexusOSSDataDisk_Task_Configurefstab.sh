cp /etc/fstab /etc/fstab.orig
echo "/dev/sdb /mnt/nexus-data xfs defaults 2 0" | tee /etc/fstab