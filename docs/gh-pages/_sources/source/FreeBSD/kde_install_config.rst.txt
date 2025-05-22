Message from fusefs-libs3-3.17.1:

--
Install the FUSE kernel module (kldload fusefs) to use this port.
=====
Message from ocl-icd-2.3.2:

--
Check your environment variable

	OLC_ICD_VENODRDIR

On FreeBSD, this is set to 

	OCL_ICD_VENDORDIR=/usr/local/etc/OpenCL/vendors

The OCL_ICD_VENDORDIR 
(ICD = Installable Client Driver) holds the platform
specific driver configuration files (i.e Intel,
nVidia, AMD, other OpenCL capable devices).

It could be set globally from your system's shell environemt
setting, for 

csh in /etc/csh.cshrc:
	setenv OCL_ICD_VENDORDIR  /usr/local/etc/OpenCL/vendors

or for sh/bash/ksh and derivatives, /etc/profile:
	export OCL_ICD_VENDORDIR=/usr/local/etc/OpenCL/vendors
=====
Message from phonon-qt6-4.12.0_3:

--
Please, consider installing backends for Phonon:
- multimedia/phonon-vlc		VLC backend
=====
Message from postgresql17-client-17.5:

--
The PostgreSQL port has a collection of "side orders":

postgresql-docs
  For all of the html documentation

p5-Pg
  A perl5 API for client access to PostgreSQL databases.

postgresql-tcltk
  If you want tcl/tk client support.

postgresql-jdbc
  For Java JDBC support.

postgresql-odbc
  For client access from unix applications using ODBC as access
  method. Not needed to access unix PostgreSQL servers from Win32
  using ODBC. See below.

ruby-postgres, py-psycopg
  For client access to PostgreSQL databases using the ruby & python
  languages.

postgresql-plperl, postgresql-pltcl & postgresql-plruby
  For using perl5, tcl & ruby as procedural languages.

postgresql-contrib
  Lots of contributed utilities, postgresql functions and
  datatypes. There you find pg_standby, pgcrypto and many other cool
  things.

etc...
=====
Message from py311-pycryptodomex-3.21.0:

--
Install the math/gmp port to enable accelerated processing with the GNU
Multiple Precision Arithmetic Library. PyCryptodome will use the
optional enhancement at runtime automatically if the library is
available.
=====
Message from kf5-kglobalaccel-5.116.0_1:

--
===>   NOTICE:

This port is deprecated; you may wish to reconsider installing it:

has its functionality stripped compared to a kf6 variant.
=====
Message from kf5-kguiaddons-5.116.0_2:

--
===>   NOTICE:

This port is deprecated; you may wish to reconsider installing it:

has its functionality stripped compared to a kf6 variant.
=====
Message from kf5-kwallet-5.116.0_3:

--
===>   NOTICE:

This port is deprecated; you may wish to reconsider installing it:

has its functionality stripped compared to a kf6 variant.
=====
Message from kf5-kio-5.116.0_1:

--
===>   NOTICE:

This port is deprecated; you may wish to reconsider installing it:

has its functionality stripped compared to a kf6 variant.
=====
Message from kio-fuse-5.1.0_2:

--
To fully use KIO-fuse, you will need FUSE and usermount enabled, e.g.
    kldload fusefs
    sysctl vfs.usermount=1
to make these changes permanent, see loader.conf(5) and sysctl.conf(5).
=====
Message from konqueror-25.04.1:

--
If you get wrong colors when watching html5 videos, this is probably because
your system does not support hardware acceleration (see bug 237277): you can
disable it by starting the browser from command line with the --disable-gpu
option.
=====
Message from smartmontools-7.5:

--
smartmontools has been installed

To check the status of drives, use the following:

	/usr/local/sbin/smartctl -a /dev/ad0	for first ATA/SATA drive
	/usr/local/sbin/smartctl -a /dev/da0	for first SCSI drive
	/usr/local/sbin/smartctl -a /dev/ada0	for first SATA drive

To include drive health information in your daily status reports,
add a line like the following to /etc/periodic.conf:
	daily_status_smart_devices="/dev/ad0 /dev/da0"
substituting the appropriate device names for your SMART-capable disks.

To enable drive monitoring, you can use /usr/local/sbin/smartd.
A sample configuration file has been installed as
/usr/local/etc/smartd.conf.sample
Copy this file to /usr/local/etc/smartd.conf and edit appropriately

To have smartd start at boot
	echo 'smartd_enable="YES"' >> /etc/rc.conf

To enable verification of the drivedb updates, install the "security/gnupg"
package.
=====
Message from webcamd-5.17.1.2_2:

--
1) To start webcamd(8) automatically at system startup:

	# sysrc webcamd_enable=YES

2) Please restart devd(8) to start webcamd(8):

	# service devd restart

3) Users requiring webcamd must be members of the "webcamd" group:

	# pw groupmod webcamd -m <username>

4) If webcamd still did not start, consult the installed webcamd rc.d
script for more help and instructions on how to start webcamd.
--
===>   NOTICE:

The webcamd port currently does not have a maintainer. As a result, it is
more likely to have unresolved issues, not be up-to-date, or even be removed in
the future. To volunteer to maintain this port, please create an issue at:

https://bugs.freebsd.org/bugzilla

More information about port maintainership is available at:

https://docs.freebsd.org/en/articles/contributing/#ports-contributing

Install sddm
-------------

New packages to be INSTALLED:
	sddm: 0.21.0.36

Installed packages to be REINSTALLED:
	lightdm-1.32.0_6
	pkg-2.1.2

Number of packages to be installed: 1
Number of packages to be reinstalled: 2

The process will require 5 MiB more space.
255 KiB to be downloaded.

Proceed with this action? [y/N]: y
[1/1] Fetching lightdm-1.32.0_6.pkg: 100%  255 KiB 261.0kB/s    00:01
Checking integrity... done (1 conflicting)
  - lightdm-1.32.0_6 conflicts with sddm-0.21.0.36 on /usr/local/share/dbus-1/system.d/org.freedesktop.DisplayManager.conf
Checking integrity... done (0 conflicting)
Conflicts with the existing packages have been found.
One more solver iteration is needed to resolve them.
The following 5 package(s) will be affected (of 0 checked):

New packages to be INSTALLED:
	sddm: 0.21.0.36

Installed packages to be REINSTALLED:
	pkg-2.1.2

Installed packages to be REMOVED:
	lightdm: 1.32.0_6
	lightdm-gtk-greeter: 2.0.9
	lightdm-gtk-greeter-settings: 1.2.2_4

Number of packages to be removed: 3
Number of packages to be installed: 1
Number of packages to be reinstalled: 1

The process will require 2 MiB more space.

Proceed with this action? [y/N]: y
Checking integrity... done (0 conflicting)
[1/5] Deinstalling lightdm-gtk-greeter-2.0.9...
:: Removing greeter configuration in /usr/local/etc/lightdm/lightdm.conf
:: Configure another greeter if you plan to keep using lightdm.
:: #greeter-session=example-gtk-gnome
==> You should manually remove the "lightdm" user
==> You should manually remove the "lightdm" group
==> You should manually remove the "video" group
===> Creating groups
Creating group 'sddm' with gid '219'
===> Creating users
Creating user 'sddm' with uid '219'
===> Creating homedir(s)
[5/5] Extracting sddm-0.21.0.36: 100%
==> Running trigger: gtk-update-icon-cache.ucl
Generating GTK icon cache for /usr/local/share/icons/hicolor
==> Running trigger: desktop-file-utils.ucl
Building cache database of MIME types
You may need to manually remove /usr/local/etc/lightdm/lightdm-gtk-greeter.conf if it is no longer needed.
=====
Message from sddm-0.21.0.36:

--
SDDM lists a "user session" which needs either an .xinitrc in the user's
home directory, or as a fallback, xterm. In order to use the "user session"
feature, a ~/.xinitrc is recommended.


Configuring SDDM
----------------

Configuring SDDM by using plasma[5|6]-sddm-kcm

If you installed sddm by binary package you have to set this rule in order to get this module functional:

Create this file /usr/local/etc/polkit-1/rules-d/40-wheel-group.rules with this content:

polkit.addRule(function(action, subject) {
    if (subject.isInGroup("wheel")) {
    	return polkit.Result.YES;
    }
});

and restart the session.
Configuring SDDM by using the configuration file

    diff /usr/local/etc/sddm.conf.sample /usr/local/etc/sddm.conf
    $EDITOR /usr/local/etc/sddm.conf

Likewise, if you installed sddm using binary packets perhaps you cannot find sddm.conf and sddm.conf.sample files. You can get one by launching

    # sddm --example-config /usr/local/etc/sddm.conf



