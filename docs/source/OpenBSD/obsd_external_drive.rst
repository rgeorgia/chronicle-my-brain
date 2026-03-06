Setting Up External Drive
=========================

How many disks do I have?

.. code-block:: bash

    rgeorgia@openHammerPOC11:~$ sysctl hw.disknames
    hw.disknames=sd0:,sd1:ddfd33f24fa82897

Now I want see which is the boot disk. 

dmesg | grep sd*
-----------------

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ dmesg | grep sd0
        sd0 at scsibus0 targ 0 lun 0: <ATA, WDC WD40EFRX-68N, 82.0> naa.50014ee2651931c3
        sd0: 3815447MB, 512 bytes/sector, 7814037168 sectors
        sd0 at scsibus1 targ 0 lun 0: <ATA, WDC WD40EFRX-68N, 82.0> naa.50014ee2651931c3
        sd0: 3815447MB, 512 bytes/sector, 7814037168 sectors
        sd0 at scsibus1 targ 0 lun 0: <ATA, WDC WD40EFRX-68N, 82.0> naa.50014ee2651931c3
        sd0: 3815447MB, 512 bytes/sector, 7814037168 sectors
        sd0 at scsibus1 targ 0 lun 0: <ATA, WDC WD40EFRX-68N, 82.0> naa.50014ee2651931c3
        sd0: 3815447MB, 512 bytes/sector, 7814037168 sectors
        sd0 at scsibus1 targ 0 lun 0: <ATA, WDC WD40EFRX-68N, 82.0> naa.50014ee2651931c3
        sd0: 3815447MB, 512 bytes/sector, 7814037168 sectors
        sd0 at scsibus1 targ 0 lun 0: <ATA, WDC WD40EFRX-68N, 82.0> naa.50014ee2651931c3
        sd0: 3815447MB, 512 bytes/sector, 7814037168 sectors

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ dmesg | grep sd1
        sd1 at scsibus0 targ 1 lun 0: <ATA, INDMEM SSD mSata, Q092> naa.0000000000000000
        sd1: 244198MB, 512 bytes/sector, 500118192 sectors, thin
        sd1 at scsibus1 targ 1 lun 0: <ATA, INDMEM SSD mSata, Q092> naa.0000000000000000
        sd1: 244198MB, 512 bytes/sector, 500118192 sectors, thin
        root on sd1a (ddfd33f24fa82897.a) swap on sd1b dump on sd1b
        sd1 at scsibus1 targ 1 lun 0: <ATA, INDMEM SSD mSata, Q092> naa.0000000000000000
        sd1: 244198MB, 512 bytes/sector, 500118192 sectors, thin
        root on sd1a (ddfd33f24fa82897.a) swap on sd1b dump on sd1b
        sd1 at scsibus1 targ 1 lun 0: <ATA, INDMEM SSD mSata, Q092> naa.0000000000000000
        sd1: 244198MB, 512 bytes/sector, 500118192 sectors, thin
        root on sd1a (ddfd33f24fa82897.a) swap on sd1b dump on sd1b
        sd1 at scsibus1 targ 1 lun 0: <ATA, INDMEM SSD mSata, Q092> naa.0000000000000000
        sd1: 244198MB, 512 bytes/sector, 500118192 sectors, thin
        root on sd1a (ddfd33f24fa82897.a) swap on sd1b dump on sd1b
        sd1 at scsibus1 targ 1 lun 0: <ATA, INDMEM SSD mSata, Q092> naa.0000000000000000
        sd1: 244198MB, 512 bytes/sector, 500118192 sectors, thin
        root on sd1a (ddfd33f24fa82897.a) swap on sd1b dump on sd1b

df -h
------

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ df -h
        Filesystem     Size    Used   Avail Capacity  Mounted on
        /dev/sd1a      7.7G    151M    7.2G     3%    /
        /dev/sd1n     87.2G   11.9M   82.9G     1%    /home
        /dev/sd1d      7.8G   10.0K    7.4G     1%    /tmp
        /dev/sd1f     33.9G    1.6G   30.6G     6%    /usr
        /dev/sd1g      1.9G    322M    1.5G    18%    /usr/X11R6
        /dev/sd1h     24.2G    2.3G   20.7G    10%    /usr/local
        /dev/sd1k      6.8G    2.0K    6.4G     1%    /usr/obj
        /dev/sd1j      6.8G    2.0K    6.4G     1%    /usr/src
        /dev/sd1e     29.1G   45.1M   27.6G     1%    /var
        /dev/sd1m      9.7G    2.0K    9.2G     1%    /var/postgresql
        /dev/sd1l      7.8G    1.4M    7.4G     1%    /var/www

So, looks like sd1 is my boot drive. The /dev/sd1 is 240G drive.

Let's prepare sd0. I want a small partition for meta data or something else that sounds really cool and smart. The rest of the drive will be for my Samba share.

Okay, I'll take a look at sd0

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ doas fdisk sd0
        Disk: sd0       Usable LBA: 34 to 7814037134 [7814037168 Sectors]
           #: type                                 [       start:         size ]
        ------------------------------------------------------------------------


        rgeorgia@openHammerPOC11:~$ doas fdisk sd0
        Disk: sd0       Usable LBA: 34 to 7814037134 [7814037168 Sectors]
           #: type                                 [       start:         size ]
        ------------------------------------------------------------------------
        20:50 rgeorgia@openHammerPOC11:~$ doas fdisk -v sd0
        Primary GPT:
        Disk: sd0       Usable LBA: 34 to 7814037134 [7814037168 Sectors]
        GUID: eb81cd67-b076-11f0-93f2-41623103e5ba
           #: type                                 [       start:         size ]
              guid                                 name
        ------------------------------------------------------------------------

        Secondary GPT:
        Disk: sd0       Usable LBA: 34 to 7814037134 [7814037168 Sectors]
        GUID: eb81cd67-b076-11f0-93f2-41623103e5ba
           #: type                                 [       start:         size ]
              guid                                 name
        ------------------------------------------------------------------------

        MBR:
        Disk: sd0	geometry: 32960/511/255 [4294852800 Sectors]
        Offset: 0	Signature: 0xAA55
                    Starting         Ending         LBA Info:
         #: id      C   H   S -      C   H   S [       start:        size ]
        -------------------------------------------------------------------------------
         0: EE      0   0   2 -  59967 146   3 [           1:  7814037167 ] EFI GPT
         1: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused
         2: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused
         3: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused


Creating a GPT
--------------

Looks like it's not been initialized. I'll be following instructions found on page 34 of *OpenBSD Mastery Filesystems* by Lucas. Seems like in order to create a new GPT all in one command

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ doas fdisk -Ay sd0
        Writing GPT.

Now look at our handy work.

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ doas fdisk sd0

        Disk: sd0       Usable LBA: 34 to 7814037134 [7814037168 Sectors]
           #: type                                 [       start:         size ]
        ------------------------------------------------------------------------
           0: OpenBSD                              [          64:   7814037071 ]

        rgeorgia@openHammerPOC11:~$ doas fdisk -v sd0

        Primary GPT:
        Disk: sd0       Usable LBA: 34 to 7814037134 [7814037168 Sectors]
        GUID: eb81cd67-b076-11f0-93f2-41623103e5ba
           #: type                                 [       start:         size ]
              guid                                 name
        ------------------------------------------------------------------------
           0: OpenBSD                              [          64:   7814037071 ]
              146aacad-d679-449a-ad69-04f0f00b098a OpenBSD Area

        Secondary GPT:
        Disk: sd0       Usable LBA: 34 to 7814037134 [7814037168 Sectors]
        GUID: eb81cd67-b076-11f0-93f2-41623103e5ba
           #: type                                 [       start:         size ]
              guid                                 name
        ------------------------------------------------------------------------
           0: OpenBSD                              [          64:   7814037071 ]
              146aacad-d679-449a-ad69-04f0f00b098a OpenBSD Area

        MBR:
        Disk: sd0	geometry: 32960/511/255 [4294852800 Sectors]
        Offset: 0	Signature: 0xAA55
                    Starting         Ending         LBA Info:
         #: id      C   H   S -      C   H   S [       start:        size ]
        -------------------------------------------------------------------------------
         0: EE      0   0   2 -  27006 208   2 [           1:  3519069871 ] EFI GPT
         1: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused
         2: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused
         3: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused

disklabel
---------

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ doas disklabel -p t sd0

        # /dev/rsd0c:
        type: SCSI
        disk: SCSI disk
        label: WDC WD40EFRX-68N
        duid: 4307e41acc9a8f74
        flags:
        bytes/sector: 512
        sectors/track: 255
        tracks/cylinder: 511
        sectors/cylinder: 130305
        cylinders: 59967
        total sectors: 7814037168 # total bytes: 3.6T
        boundstart: 64
        boundend: 7814037135

        16 partitions:
        #                size           offset  fstype [fsize bsize   cpg]
          a:             3.6T               64  4.2BSD   8192 65536     1
          c:             3.6T                0  unused


Creating partitions
--------------------

We will use disklabel -E to edit the partition table.

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ doas disklabel -E sd0

        Label editor (enter '?' for help at any prompt)
        sd0> p g
        OpenBSD area: 64-7814037135; size: 3726.0G; free: 0.0G
        #                size           offset  fstype [fsize bsize   cpg]
          a:          3726.0G               64  4.2BSD   8192 65536     1
          c:          3726.0G                0  unused
        sd0> d
        partition to delete: [] a
        sd0*> p
        OpenBSD area: 64-7814037135; size: 7814037071; free: 7814037071
        #                size           offset  fstype [fsize bsize   cpg]
          c:       7814037168                0  unused
        sd0*> a
        partition to add: [a]
        offset: [64]
        size: [7814037071] 2g
        FS type: [4.2BSD]
        sd0*> p
        OpenBSD area: 64-7814037135; size: 7814037071; free: 7809737071
        #                size           offset  fstype [fsize bsize   cpg]
          a:          4300000               64  4.2BSD   2048 16384     1
          c:       7814037168                0  unused
        sd0*> a
        partition to add: [b] d
        offset: [4300064]
        size: [7809737071]
        FS type: [4.2BSD]
        sd0*> p
        OpenBSD area: 64-7814037135; size: 7814037071; free: 111
        #                size           offset  fstype [fsize bsize   cpg]
          a:          4300000               64  4.2BSD   2048 16384     1
          c:       7814037168                0  unused
          d:       7809736960          4300160  4.2BSD   8192 65536     1
        sd0*> p g
        OpenBSD area: 64-7814037135; size: 3726.0G; free: 0.0G
        #                size           offset  fstype [fsize bsize   cpg]
          a:             2.1G               64  4.2BSD   2048 16384     1
          c:          3726.0G                0  unused
          d:          3724.0G          4300160  4.2BSD   8192 65536     1
        sd0*> p t
        OpenBSD area: 64-7814037135; size: 3.6T; free: 0.0T
        #                size           offset  fstype [fsize bsize   cpg]
          a:             0.0T               64  4.2BSD   2048 16384     1
          c:             3.6T                0  unused
          d:             3.6T          4300160  4.2BSD   8192 65536     1
        sd0*> ?
        Available commands:
         ? | h    - show help                 n [part] - set mount point
         A        - auto partition all space  p [unit] - print partitions
         a [part] - add partition             q        - quit & save changes
         b        - set OpenBSD boundaries    R [part] - resize auto allocated partition
         c [part] - change partition size     r        - display free space
         D        - reset label to default    s [path] - save label to file
         d [part] - delete partition          U        - undo all changes
         e        - edit label description    u        - undo last change
         i        - modify disklabel UID      w        - write label to disk
         l [unit] - print disk label header   x        - exit & lose changes
         M        - disklabel(8) man page     z        - delete all partitions
         m [part] - modify partition

        Suffixes can be used to indicate units other than sectors:
         'b' (bytes), 'k' (kilobytes), 'm' (megabytes), 'g' (gigabytes) 't' (terabytes)
         'c' (cylinders), '%' (% of total disk), '&' (% of free space).
        Values in non-sector units are truncated to the nearest cylinder boundary.

        sd0*> w
        sd0> p
        OpenBSD area: 64-7814037135; size: 7814037071; free: 111
        #                size           offset  fstype [fsize bsize   cpg]
          a:          4300000               64  4.2BSD   2048 16384     1
          c:       7814037168                0  unused
          d:       7809736960          4300160  4.2BSD   8192 65536     1
        sd0> p g
        OpenBSD area: 64-7814037135; size: 3726.0G; free: 0.0G
        #                size           offset  fstype [fsize bsize   cpg]
          a:             2.1G               64  4.2BSD   2048 16384     1
          c:          3726.0G                0  unused
          d:          3724.0G          4300160  4.2BSD   8192 65536     1
        sd0> q
        No label changes.

New disk layout
---------------

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ doas disklabel sd0
        # /dev/rsd0c:
        type: SCSI
        disk: SCSI disk
        label: WDC WD40EFRX-68N
        duid: 4307e41acc9a8f74
        flags:
        bytes/sector: 512
        sectors/track: 255
        tracks/cylinder: 511
        sectors/cylinder: 130305
        cylinders: 59967
        total sectors: 7814037168
        boundstart: 64
        boundend: 7814037135

        16 partitions:
        #                size           offset  fstype [fsize bsize   cpg]
          a:          4300000               64  4.2BSD   2048 16384     1
          c:       7814037168                0  unused
          d:       7809736960          4300160  4.2BSD   8192 65536     1

New file system
---------------

Now I'll "format" the new partitions. Note: using the -q flag will suppress the output.

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ doas newfs /dev/rsd0a
           
        /dev/rsd0a: 2099.6MB in 4300000 sectors of 512 bytes
        11 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
        super-block backups (for fsck -b #) at:
         160, 414880, 829600, 1244320, 1659040, 2073760, 2488480, 2903200, 3317920, 3732640, 4147360,

        rgeorgia@openHammerPOC11:~$ doas newfs /dev/rsd0d
        /dev/rsd0d: 3813348.0MB in 7809736960 sectors of 512 bytes
        1168 cylinder groups of 3266.88MB, 52270 blocks, 104704 inodes each
        super-block backups (for fsck -b #) at:
         256, 6690816, 13381376, 20071936, 26762496, 33453056, 40143616, 46834176, 53524736, 60215296, 66905856, 73596416, 80286976,86977536, 93668096, 100358656, 107049216, <snip> 7781121536, 7787812096, 7794502656, 7801193216, 7807883776,

Finding DUID
------------

.. code-block:: bash

rgeorgia@openHammerPOC11:~$ doas disklabel sd0 | grep duid
duid: 4307e41acc9a8f74


Update fstab
------------

We have the DUID, let's update the ``/etc/fstab`` to include our new partitions

rgeorgia@openHammerPOC11:~$ cat /etc/fstab

ddfd33f24fa82897.b none swap sw
ddfd33f24fa82897.a / ffs rw 1 1
ddfd33f24fa82897.n /home ffs rw,nodev,nosuid 1 2
ddfd33f24fa82897.d /tmp ffs rw,nodev,nosuid 1 2
ddfd33f24fa82897.f /usr ffs rw,nodev 1 2
ddfd33f24fa82897.g /usr/X11R6 ffs rw,nodev 1 2
ddfd33f24fa82897.h /usr/local ffs rw,wxallowed,nodev 1 2
ddfd33f24fa82897.k /usr/obj ffs rw,nodev,nosuid 1 2
ddfd33f24fa82897.j /usr/src ffs rw,nodev,nosuid 1 2
ddfd33f24fa82897.e /var ffs rw,nodev,nosuid 1 2
ddfd33f24fa82897.m /var/postgresql ffs rw,nodev,nosuid 1 2
ddfd33f24fa82897.l /var/www ffs rw,nodev,nosuid 1 2
4307e41acc9a8f74.a /var/hammer/hmeta ffs rw,nodev,nosuid 1 2
4307e41acc9a8f74.d /var/hammer/martel ffs rw,nodev,nosuid 1 2

Mount all
---------

Use ``mount -a`` to mount everything listed in ``/etc/fstab``. Then check your work.

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ doas mount -a

        rgeorgia@openHammerPOC11:~$ mount
        
        /dev/sd1a on / type ffs (local)
        /dev/sd1n on /home type ffs (local, nodev, nosuid)
        /dev/sd1d on /tmp type ffs (local, nodev, nosuid)
        /dev/sd1f on /usr type ffs (local, nodev)
        /dev/sd1g on /usr/X11R6 type ffs (local, nodev)
        /dev/sd1h on /usr/local type ffs (local, nodev, wxallowed)
        /dev/sd1k on /usr/obj type ffs (local, nodev, nosuid)
        /dev/sd1j on /usr/src type ffs (local, nodev, nosuid)
        /dev/sd1e on /var type ffs (local, nodev, nosuid)
        /dev/sd1m on /var/postgresql type ffs (local, nodev, nosuid)
        /dev/sd1l on /var/www type ffs (local, nodev, nosuid)
        /dev/sd0a on /var/hammer/hmeta type ffs (local, nodev, nosuid)
        /dev/sd0d on /var/hammer/martel type ffs (local, nodev, nosuid)

        rgeorgia@openHammerPOC11:~$ df -h
        
        Filesystem     Size    Used   Avail Capacity  Mounted on
        /dev/sd1a      7.7G    151M    7.2G     3%    /
        /dev/sd1n     87.2G   11.9M   82.9G     1%    /home
        /dev/sd1d      7.8G   10.0K    7.4G     1%    /tmp
        /dev/sd1f     33.9G    1.6G   30.6G     6%    /usr
        /dev/sd1g      1.9G    322M    1.5G    18%    /usr/X11R6
        /dev/sd1h     24.2G    2.3G   20.7G    10%    /usr/local
        /dev/sd1k      6.8G    2.0K    6.4G     1%    /usr/obj
        /dev/sd1j      6.8G    2.0K    6.4G     1%    /usr/src
        /dev/sd1e     29.1G   45.1M   27.6G     1%    /var
        /dev/sd1m      9.7G    2.0K    9.2G     1%    /var/postgresql
        /dev/sd1l      7.8G    1.4M    7.4G     1%    /var/www

Reboot
------

Of course we need to reboot to verify it is all put together correctly.
After the reboot...

.. code-block:: bash

        rgeorgia@openHammerPOC11:~$ df -h

        Filesystem     Size    Used   Avail Capacity  Mounted on
        /dev/sd1a      7.7G    120M    7.2G     2%    /
        /dev/sd1n     87.2G   11.9M   82.9G     1%    /home
        /dev/sd1d      7.8G   10.0K    7.4G     1%    /tmp
        /dev/sd1f     33.9G    1.6G   30.6G     6%    /usr
        /dev/sd1g      1.9G    322M    1.5G    18%    /usr/X11R6
        /dev/sd1h     24.2G    2.3G   20.7G    10%    /usr/local
        /dev/sd1k      6.8G    2.0K    6.4G     1%    /usr/obj
        /dev/sd1j      6.8G    2.0K    6.4G     1%    /usr/src
        /dev/sd1e     29.1G   45.1M   27.6G     1%    /var
        /dev/sd1m      9.7G    2.0K    9.2G     1%    /var/postgresql
        /dev/sd1l      7.8G    1.4M    7.4G     1%    /var/www
        /dev/sd0a      2.0G    2.0K    1.9G     1%    /var/hammer/hmeta
        /dev/sd0d      3.6T    8.0K    3.4T     1%    /var/hammer/martel


