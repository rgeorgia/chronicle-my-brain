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

.. code-block:: bash

        cfdisk /dev/nvme0n1

        nvme0n1p1    1G  fat32   efi partion
        nvme0n1p2    8G  swap    2 times ram
        nvme0n1p3    *   ext4    root

        mkfs.vfat -F 32 /dev/nvme0n1p1
        mkswap          /dev/nvme0n1p2
        mkfs.ext4       /dev/nvme0n1p3

Mount Drives
-------------

.. code-block:: bash

        mount /dev/nvme0n1p3 /mnt/gentoo
        swapon /dev/nvme0n1p2
        mkdir -p /mnt/gentoo/boot/efi

Grab Stage
----------

Make sure you are in the proper directory

.. code-block:: bash

        cd /mnt/gentoo

        date MMDDhhmmCCYY

        links https://www.gentoo.org/downloads/mirrors/

        tar xpvf <stage> --xattrs-include='*.*' --numeric-owner

Update make.conf
----------------

.. code-block:: bash

        COMMON_FLAGS="-march=native -O2 -pipe"
        MAKEOPTS="-j8"
        USE="-systemd -KDE X gtk gnome"

        cp --dereference /etc/resolv.conf /mnt/gentoo/etc

Mount Stuff
-----------

.. code-block:: bash

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

        mount /dev/nvme0n1p1 /boot/efi

        emerge-webrsync

        eselect profile list
        eselect profile set 23
        emerge --sync
        echo 'sys-kernel/linux-firmware @BINARY-REDISTRIBUTABLE' | tee -a /etc/portage/package.license

Note: set portage env var ACCEPT_LICENSE


Note: /var/db/repos/gentoo/profiles/use.desc describes all USE flags

Note: What about video card in /etc/portage/package.use/00video_cards?

.. code-block:: bash

        emerge --ask app-editors/vim
        emerge --ask --verbose --update --deep --changed-use @world

Locale
------

.. code-block:: bash

        ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

        vim /etc/locale.gen
        locale-gen
        eselect locale list
        eselect locale set 4

Update env
----------
.. code-block:: bash

        env-update && source /etc/profile && export PS1="(chroot) $PS1"

Configure Kernel
----------------

.. code-block:: bash

        emerge --ask sys-kernel/linux-firmware
        emerge --ask sys-firmware/sof-firmware

GRUB
----

.. code-block:: bash

        echo "sys-kernel/installkernel dracut grub" >> /etc/portage/package.use/installkernel

        emerge --ask sys-kernel/installkernel
        emerge --ask sys-kernel/gentoo-kernel-bin

Configure System
----------------

.. code-block:: bash

        vim /etc/fstab

        /dev/nvme0n1p1   /boot/efi   vfat    defaults            0 2
        /dev/nvme0n1p2   none        swap    sw                  0 0
        /dev/nvme0n1p3   /           ext4    defaults,noatime    0 1

Network
-------

.. code-block:: bash

        echo "YOURHOSTNAME" > /etc/hostname

Edit /etc/hosts
----------------

.. code-block:: bash

        127.0.0.1   YOURHOSTNAME localhost


Edit /etc/conf.d/hostname
--------------------------

.. code-block:: bash

        emerge --ask net-misc/dhcpcd
        emerge --ask net-misc/networkmanager

        rc-update add NetworkManager default
        rc-update add dhcpcd default

        rc-service NetworkManager start
        rc-service dhcpcd start

Adding Users:
---------------

Note: before adding users, add the shells you want

Change root password

.. code-block:: bash

        passwd root

        emerge --ask app-shells/fish bash

        useradd -m -G wheel,video,audio,kvm,plugdev -s /usr/bin/fish rgeorgia
        passwd rgeorgia

        emerge --ask app-admin/sysklogd
        emerge --ask sys-apps/mlocate
        emerge --ask net-misc/chrony
        emerge --ask app-admin/sudo

        rc-update add sysklogd default
        rc-update add chronyd default
        rc-update add sshd default

        EDITOR=vim visudo

Boot Loader
-----------

.. code-block:: bash

        echo 'GRUB_PLATFORMS="efi-64"' >> /etc/portage/make.conf

        emerge --ask sys-boot/grub efibootmgr
        grub-install --efi-directory /boot/efi
        grub-mkconfig -o /boot/grub/grub.cfg

REBOOT
------

Exit chroot

.. code-block:: bash

        exit

        cd to home or /root

        umount -l /mnt/gentoo/{shm,pts}
        umount -R /mnt/gentoo

        reboot

POST INSTALL
------------

.. code-block:: bash

        sudo touch /etc/portage/package.use/xorg
        echo 'sys-auth/pambase elogind' | tee -a /etc/portage/package.use/xorg
        echo 'media-libs/libglvd x' | tee -a /etc/portage/package.use/xorg
        echo 'sys-apps/dbus' | tee -a /etc/portage/package.use/xorg

        sudo emerge --ask sys-apps/dbus
        sudo emerge --ask dev-vcs/git
        sudo emerge --ask x11-base/xorg-server
        sudo emerge --ask x11-drivers/xf86-video-intel
        sudo emerge --ask x11-apps/xinit
        sudo emerge --ask x11-apps/xrandr
        sudo emerge --ask gnome-base/gdm
        sudo emerge --ask gnome-base/gnome
        sudo emerge --ask --noreplace gui-libs/display-manager

Display Manager
---------------

.. code-block:: bash

        vim /etc/conf.d/display-manager
        DISPLAYMANAGER="gdm"
        sudo rc-update add display-manager default

Add for video card to package.use
----------------------------------

.. code-block:: bash

        echo "*/* VIDEO_CARDS: -* intel" >> /etc/portage/package.use/00video-cards

**Note**: add binary package

Note: if you want .xinitrc add ``exec sway``

