Rewrite hbsd-upgrade
====================

Project Link: `New Binary Updater <https://hardenedbsd.org/article/shawn-webb/2015-12-31/introducing-hardenedbsds-new-binary-updater>`_

First attempt: flua
-----------------------

flua DESCRIPTION
~~~~~~~~~~~~~~~~~

**flua** is a minimal Lua interpreter integrated into the FreeBSD base
system.  It is derived from Lua 5.4 with modifications to suit the needs
of FreeBSD build infrastructure and system tooling.  flua is intended for
internal use within the base system and is not designed for general-
purpose scripting or use by third-party applications.

Unlike full Lua installations provided by the Ports Collection, flua has
a reduced feature set and is limited to meeting the requirements of base
system environments such as the bootloader.

INCLUDED MODULES
~~~~~~~~~~~~~~~~

Lua modules as well as bespoke modules necessary for the base system:

- lfs (LuaFileSystem) – file attribute and directory manipulation
- lposix - basic POSIX system calls
- freebsd.kenv(3lua)
- freebsd.sys.linker(3lua)
- hash(3lua)
- jail(3lua)

-------------------------------------------------------------------------

Step One: Transfer Functionality
---------------------------------

Transfer the same functionality of the hbsd-update and hbsd-update-build from shell to flua.

Current Script Structure
~~~~~~~~~~~~~~~~~~~~~~~~~

.. dropdown:: hbsd-update functions
   
    .. csv-table:: 
        :file: ./hbsd-update-fn.csv
        :widths: auto
        :header: "Function Name", "Description"

    .. csv-table:: 
        :file: ./hbsd-update-build-fn.csv
        :widths: auto
        :header: "Function Name", "Description"

