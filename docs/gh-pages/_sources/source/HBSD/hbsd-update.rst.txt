Rewrite hbsd-upgrade
====================

Project Link: `New Binary Updater <https://hardenedbsd.org/article/shawn-webb/2015-12-31/introducing-hardenedbsds-new-binary-updater>`_

First attempt: flua
-----------------------

DESCRIPTION
~~~~~~~~~~~~~

``flua`` is a minimal Lua interpreter integrated into the FreeBSD base
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

Step One:
---------

Transfer the same functionality from the hbsd-update and hbsd-update-build from shell to flua.

Current Script Structure
------------------------

.. dropdown:: hbsd-update functions
   
        - is_true() 
        - debug_print() 
        - usage() 
        - sigint_handler() 
        - get_tmpdir() 
        - get_last_field() 
        - dnssec_check() 
        - get_version() 
        - check_version() 
        - check_jailname() 
        - fetch_update() 
        - check_securelevel() 
        - check_pubkey_validity() 
        - validate_file() 
        - check_set_validity() 
        - apply_mtree() 
        - apply_base() 
        - set_kernel_config() 
        - apply_kernel() 
        - apply_integriforce() 
        - remove_obsolete() 
        - create_be() 
        - cache_version() 
        - activate_be() 
        - destroy_be() 
        - cleanup() 
        - check_sanity() 
        - report_version_machine_readable() 
        - report_version() 
        - pre_install_hook() 
        - post_install_hook() 
        - main() 

.. dropdown:: hbsd-update-build functions

        - debug_print() 
        - usage() 
        - setup_environment() 
        - cleanup_chroot() 
        - setup_directories() 
        - setup_chroot() 
        - clone_source() 
        - build_source() 
        - create_src_conf() 
        - install_binutils() 
        - prep_release() 
        - build_base_archive() 
        - build_etcupdate_archive() 
        - build_kernel_archives() 
        - build_obsolete() 
        - build_src_tarball() 
        - build_mtree() 
        - add_extra_files() 
        - check_integriforce_rule_exists() 
        - build_integriforce_rules() 
        - sign_artifacts() 
        - git_version() 
        - hbsd_version() 
        - full_version() 
        - update_filename() 
        - build_update_archive() 
        - sanity_check() 
        - sanity_check_archive() 
        - log_build() 
        - main() 


