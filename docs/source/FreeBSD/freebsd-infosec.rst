Infosec on FreeBSD
=======================

Tools to install
-----------------

- [X] john
- [X] ndiff
- [X] nmap
- [M] zenmap
- [X] nikto
- [X] kismet-2008
- [M] wistumbler2-gtk
- [X] wireshark
- [ ] sqlmap
- [ ] ettercap-gtk
- [ ] traceroute
- [ ] traceroute6
- [ ] hashcat
- [ ] hydra
- [ ] burp
- [ ] nbtscan
- [ ] dillo
- [X] zap
- [ ] chromium
- [ ] sqlitebrowser
 

ZAP port was installed
-----------------------

1) You must install Chrome based browser or Firefox based browser for be used in some tasks.

.. code-block:: bash

  # pkg install chromium firefox geckodriver

2) ZAP includes linux webdrivers for Chrome and Firefox but these don't work
   on FreeBSD.

   You must change some paths from `Tools/Options/Selenium/Webdrivers`:

.. code-block:: bash

   Chromedriver to /usr/local/bin/chromedriver
   Geckodriver to /usr/local/bin/geckodriver

   Also, you must change Chrome and Firefox based web browser binary path files:

   Chrome binary to /usr/local/bin/chrome
   Firefox binary to /usr/local/bin/firefox

3) If you want to use some python scripts to use ZAP from command line or from
   another applications, look at the following urls:

   https://github.com/zaproxy/zaproxy/blob/main/docker/zap-baseline.py
   https://github.com/zaproxy/community-scripts/tree/main/other/api/mass-baseline
   https://github.com/zaproxy/zap-api-python/tree/main/src/examples

   These scripts use ZAP Python API. Install it from security/py-zaproxy

4) Enjoy it

Kismet
------

Kismet has been installed with a setuid-root capture helper binary,
`/usr/local/bin/kismet_capture`, which may be executed by users in the
kismet group.  USERS IN THIS GROUP WILL BE ABLE TO ALTER NETWORK
INTERFACE STATES, but this is more secure than running all of kismet
as root.  ONLY users in this group will be able to run kismet and capture
from physical network devices.

Wireshark
----------

In order for wireshark be able to capture packets when used by unprivileged
user, /dev/bpf should be in network group and have read-write permissions.
For example:

# chgrp network /dev/bpf*
# chmod g+r /dev/bpf*
# chmod g+w /dev/bpf*

In order for this to persist across reboots, add the following to
/etc/devfs.conf:

own  bpf* root:network
perm bpf* 0660


