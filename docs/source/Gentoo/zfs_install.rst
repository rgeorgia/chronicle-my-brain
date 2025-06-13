Gentoo ZFS Install
==================

ZFS on root
-----------

ref: `ZFS/rootfs <https://wiki.gentoo.org/wiki/ZFS/rootfs#Live_Media>`_

Partitions
~~~~~~~~~~
Layout

Follow the Handbook section on Preparing the disks returning at the creating file systems section.
This guide will be using the example below however it should be simple enough to adapt this to the user's needs.

|device     |size           |partition               |mount point          |
|-----------|---------------|------------------------|---------------------|
/dev/sda1   | 1024 MiB      | EFI System Partition   | /boot/efi           | 
/dev/sda2   | 2048 MiB      | swap                   | swap                |
/dev/sda3   | Rest of Disk  | ZFS Partition          | /, /boot, /home, ...|

The document used /efi as the mount point, but other docs use /boot/efi.

Boot
~~~~~~~~~~

.. code-block:: bash


Swap
~~~~~~~~~~

.. code-block:: bash

