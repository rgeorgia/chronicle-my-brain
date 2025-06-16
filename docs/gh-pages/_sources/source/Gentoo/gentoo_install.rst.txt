Gentoo Install
==============

General Prep
------------

lsblk
ping www.gentoo.org
ifconfig to get interfaces

If you want to remotely install start sshd and set the root password

Prepare Disks
-------------

cfdisk /dev/sda

sda1    1G  fat32   efi partion
sda2    8G  swap    2 times ram
sda3    *   ext4    root

mkfs.vfat -F 32 /dev/sda1
mkswap          /dev/sda2
mkfs.ext4       /dev/sda3

Mount Drives
-------------

mount /dev/sda3 /mnt/gentoo
swapon /dev/sda2
mkdir -p /mnt/gentoo/boot/efi

Grab Stage
----------

Make sure you are in the proper directory

cd /mnt/gentoo

date MMDDhhmmCCYY

links https://www.gentoo.org/downloads/mirrors/

tar xpvf <stage> --xattrs-include='*.*' --numeric-owner

Update make.conf
----------------
COMMON_FLAGS="-march=native -O2 -pipe"
MAKEOPTS="-j8"
USE="-systemd -KDE X gtk gnome"

cp --dereference /etc/resolv.conf /mnt/gentoo/etc

Mount Stuff
-----------

mount --types proc  /proc   /mnt/gentoo/proc
mount --rbind       /sys    /mnt/gentoo/sys
mount --make-rslave         /mnt/gentoo/sys
mount --rbind       /dev    /mnt/gentoo/dev
mount --make-rslave         /mnt/gentoo/dev
mount --bind        /run    /mnt/gentoo/run
mount --make-slave          /mnt/gentoo/run

chroot /mnt/gentoo /bin/bash
source /etc/profile
export PS1="(chroot) $PS1"

mount /dev/sda1 /boot/efi

emerge-webrsync

eselect profile list
eselect profile set 23
emerge --sync
echo 'sys-kernel/linux-firmware @BINARY-REDISTRIBUTABLE' | tee -a /etc/portage/package.license

Note: set portage env var ACCEPT_LINCENSE
Note: /var/db/repos/gentoo/profiles/use.desc describes all USE flags
Note: What about video card in /etc/portage/package.use/00video_cards?

emerge --ask app-editors/vim
emerge --ask --verbose --update --deep --changed-used @world

Locale
------

ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

vim /etc/locale.gen
locale-gen
eselect locale list
eselect locale set 4

Update env
----------
env-update && source /etc/profile && export PS1="(chroot) $PS1"

Configure Kernel
----------------

emerge --ask sys-kernel/linux-firmware
emerge --ask sys-firmware/sof-firmware

GRUB
----

echo "sys-kernel/installkernel dracut grub" >> /etc/portage/package.use/installkernel

emerge --ask sys-kernel/installkernel
emerge --ask sys-kernel/gentoo-kernel-bin

Configure System
----------------

vim /etc/fstab

/dev/sda1   /boot/efi   vfat    defaults            0 2
/dev/sda2   none        swap    sw                  0 0
/dev/sda3   /           ext4    defaults,noatime    0 1



Network
-------

echo "YOURHOSTNAME" > /etc/hostname

Edit /etc/hosts

127.0.0.1   YOURHOSTNAME localhost

Edit /etc/conf.d/hostname

emerge --ask net-misc/dhcpcd
emerge --ask net-misc/networkmanager

rc-update add NetworkManager default
rc-update add dhcpcd default

rc-service NetworkManager start
rc-service dhcpcd start

Adding Users:

Note: before adding users, add the shells you want

Change root password

passwd root

emerge --ask app-shells/fish bash

useradd -m -G wheel,video,audio -s /usr/bin/fish rgeorgia
passwd rgeorgia

emerge --ask app-admin/sysklogd
emerge --ask sys-apps/mlocate
emerge --ask net-misc/chrony
emerge --ask app-admin/sudo

rc-update add sysklogd default
rc-update add chronyd default
rc-update add sshd default

EDITOR-vim visudo

Boot Loader
-----------

echo 'GRUB_PLATFORMS="efi-64"' >> /etc/portage/make.conf

emerge --ask sys-boot/grub efibootmgr
grub-install --efi-directory /boot/efi
grub-mkconfig -o /boot/efi/EFI

REBOOT
------

Exit chroot

exit

cd to home or /root

mount -l /mnt/gentoo/{/shm,/pts}
mount -R /mnt/gentoo

reboot

POST INSTALL
------------

sudo touch /etc/portage/package.use/xorg
echo 'sys-auth/pambase elogind' | tee -a /etc/portage/package.use/xorg
echo 'media-libs/libglvd x' | tee -a /etc/portage/package.use/xorg

sudo emerge --ask sys-apps/dbus
sudo emerge --ask dev-vcs/git
sudo emerge --ask x11-base/xorg-server
sudo emerge --ask x11-drivers/xf86-video-intel
sudo emerge --ask x11-apps/xinitr
sudo emerge --ask x11-apps/xrandr
sudo emerge --ask gnome-base/gdm
sudo emerge --ask gnome-base/gnome
sudo emerge --ask --no-replace gui-libs/display-mmanager

Display Manager
---------------

vim /etc/conf.d/display-manager
DISPLAYMANAGER="gdm"
sudo rc-update add display-manager default

Add for video card to package.use

echo "*/* VIDEO_CARDS: -* intel" >> /etc/portage/package.use/00video-cards

**Note**: add binary package

Note: if you want .xinitrc add ``exec sway``



