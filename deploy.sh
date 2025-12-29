TARGET=192.168.6.176
tar czvf /tmp/cmb.tar.gz /var/vroot
scp /tmp/cmb.tar.gz $TARGET:lz/.
