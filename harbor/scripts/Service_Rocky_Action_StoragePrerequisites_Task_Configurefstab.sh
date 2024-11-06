sudo cp /etc/fstab /etc/fstab.orig
echo "/dev/sdb /mnt/data xfs defaults 2 0" | sudo tee /etc/fstab