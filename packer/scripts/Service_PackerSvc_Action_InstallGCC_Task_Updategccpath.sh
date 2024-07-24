#PATH=$PATH:/opt/rh/devtoolset-11/root/usr/bin 
#export PATH 
ln -s /opt/rh/devtoolset-11/root/usr/bin/gcc /usr/bin/gcc
scl enable devtoolset-11 bash &
sleep 5
gcc --version

