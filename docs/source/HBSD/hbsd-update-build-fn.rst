Update Build Functions
======================

Detailed
--------

.. dropdown:: setup_chroot

        setup_chroot() prepares and populates a chroot environment for building or installing a system:

        - Ensures ${CHROOTDIR}/dev exists and mounts devfs there if it isn’t already mounted.
        - Changes to the source directory ${SRCDIR}.
        - If WANT_CHROOT_BUILD is enabled:
            - Checks out (clones) the system source tree.
            - Builds a “bootstrap” world using make buildworld, honoring parallel jobs, silent mode, and a development-mode flag.
        - Installs the built system into the chroot using make installworld distribution DESTDIR=${CHROOTDIR}.
        - Aborts and returns a nonzero status if installation fails.
        - Creates ${CHROOTDIR}/usr/obj for build artifacts.
        - Returns success (0) on completion.

        In short, it mounts required device support, optionally builds the system, installs it into a chroot, and ensures required directories exist.

.. dropdown:: clone_source

        clone_source() ensures a Git source tree exists and is up to date under a given destination directory:

        - Takes an optional argument destdir (defaults to /), and works in ${destdir}/usr/src.
        - If ${destdir}/usr/src is not already a Git repository:

            - Clones the repository from ${REPO} into ${destdir}/usr/src.
            - Checks out the specified branch ${BRANCH} (creating it from origin/${BRANCH} if needed).

        - If the repository already exists:

            - Changes into ${destdir}/usr/src and updates it with git pull.

        - Propagates any Git errors by returning a non-zero status.
        - Returns 0 on success.

        In short, it clones the source tree if missing, switches to the desired branch, or pulls updates if it already exists.


