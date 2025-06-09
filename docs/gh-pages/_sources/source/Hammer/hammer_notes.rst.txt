Notes on creating a Hammer File Share
======================================

I asked Copilot to help me create a samba file share on a VoidLinux system with a  two 8TB drives in a mirrored zpool. I want to set up a samba share that a windows machine, Mac and Linux can mount. 

First Response
-----------------

Setting up a Samba share on your Void Linux workstation with a mirrored ZFS pool for cross-platform access is a solid choice. Here’s a step-by-step guide:

1. Install Samba

First I updated the package list and installed Samba:

.. code-block:: bash

   sudo xbps-install -Syu 
   sudo xbps-install -S samba

2. Enable and Start the Samba Service

.. code-block:: bash

    sudo ln -s /etc/sv/smbd /var/service/
    sudo ln -s /etc/sv/nmbd /var/service/

To verify it's running:

.. code-block:: bash

    sudo sv status smbd
    sudo sv status nmbd

Why Separate Services?
~~~~~~~~~~~~~~~~~~~~~~~~

- smbd handles actual file sharing.
- nmbd broadcasts the share name for discovery on Windows and macOS networks.

3. Configure Your Samba Share

Edit /etc/samba/smb.conf to define your shared folder:

.. code-block:: bash

    sudo sv status smbd
    sudo sv status nmbd

.. code-block:: ini

    [global]
    workgroup = WORKGROUP
    server string = Void Samba Server
    security = user
    map to guest = Bad User

    [shared]
    path = /mnt/zpool/share
    browseable = yes
    writable = yes
    read only = no
    guest ok = yes
    force user = your_user
    valid users = your_user


My zfs dataset  is mounted at ``/zhammer``.

.. code-block:: bash

    hammerVoid ~  zfs list                                                                   Sun 08 Jun 2025 01:32:15 PM EDT
    NAME                           USED  AVAIL  REFER  MOUNTPOINT
    tank                          12.5G   887G    24K  /tank
    tank/home                     12.5G   887G    24K  /export/home
    tank/home/rgeorgia            12.5G   887G    24K  /export/home/rgeorgia
    tank/home/rgeorgia/workspace  12.5G   887G  12.5G  /export/home/rgeorgia/workspace
    zhammer                       1.52M  14.4T    96K  /zhammer
    hammerVoid ~  sudo mkdir /zhammer/martel                                                 Sun 08 Jun 2025 01:49:08 PM EDT
    Password:
    hammerVoid ~  sudo zfs create zhammer/martel                                      5.3s  Sun 08 Jun 2025 01:52:14 PM EDT
    hammerVoid ~  zfs list                                                           333ms  Sun 08 Jun 2025 01:52:25 PM EDT
    NAME                           USED  AVAIL  REFER  MOUNTPOINT
    tank                          12.5G   887G    24K  /tank
    tank/home                     12.5G   887G    24K  /export/home
    tank/home/rgeorgia            12.5G   887G    24K  /export/home/rgeorgia
    tank/home/rgeorgia/workspace  12.5G   887G  12.5G  /export/home/rgeorgia/workspace
    zhammer                       1.66M  14.4T    96K  /zhammer
    zhammer/martel                  96K  14.4T    96K  /zhammer/martel
    hammerVoid ~  sudo zfs set mountpoint=/zhammer/martel zhammer/martel 

Make sure /mnt/zpool/share exists:
.. code-block:: bash

    mkdir -p /mnt/zpool/share
    chmod 777 /mnt/zpool/share


4. Set Up User Authentication

Create a Samba user:

.. code-block:: bash

    sudo smbpasswd -a your_user


5. Adjust Firewall Settings (if applicable)

Allow Samba traffic:

.. code-block:: bash

    sudo iptables -A INPUT -p tcp --dport 445 -j ACCEPT
    sudo iptables -A INPUT -p udp --dport 137 -j ACCEPT
    sudo iptables -A INPUT -p udp --dport 138 -j ACCEPT

    sudo ufw allow 445/tcp
    sudo ufw allow 137/udp
    sudo ufw allow 138/udp
    sudo ufw allow 139/udp
    sudo ufw app list
    sudo ufw app info Samba
    sudo ufw allow Samba



6. Restart Samba

.. code-block:: bash

    sudo sv restart samba


7. Mount the Share on Other Machines

- Windows: Open Explorer, type \\your_void_ip\shared, and map the drive.
- Mac: Use Finder -> Go -> Connect to Server, then smb://your_void_ip/shared
- Linux: Mount manually:

.. code-block:: bash

    sudo mount -t cifs //your_void_ip/shared /mnt -o username=your_user,password=your_password

Let me know if you run into any issues, especially with ZFS permissions or network access!


More Secure Options
---------------------

Instead of 777, consider:
- User Group-Based Control: Create a Samba-specific group:

.. code-block:: bash

    sudo groupadd smbshare
    sudo usermod -aG smbshare your_user
    sudo chown -R your_user:smbshare /mnt/zpool/share
    sudo chmod 770 /mnt/zpool/share

- This allows only your_user and members of smbshare to access the folder.
- Force Specific Ownership in Samba: Modify your smb.conf:

.. code-block:: ini

    force group = smbshare
    create mask = 0660
    directory mask = 0770

- This ensures new files are created with proper permissions.

If you're the only one using the share and security isn't a major concern, 777 is fine for quick access. But if you prefer more control, these adjustments are better long-term solutions.
