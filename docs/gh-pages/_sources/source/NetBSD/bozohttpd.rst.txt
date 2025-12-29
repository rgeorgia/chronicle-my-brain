Setting up bozohttpd
=====================

I need to setup a web server so I can provide an interface for the user to setup the samba share or look at files or something... Sounds complicated. I'll simple setup a website for either Rocket, Axiom or Django.

I need to be able to drop the new files from the `Chronicle My Brain` project on to the RPI3 NetBSD box.

- I could use rsync, but that requires elevated privileges or creating a "login" to push the files.
- I decided to be *creative* but maybe over complicated; however, it works.

  - Create a deploy.sh on the workstation that tars the ``/var/vroot`` directory to ``/tmp/cmb.tar.gz``.
  - Transfer that file to the web server via scp using the local $USER. Make sure you have ssh keys copied so you do not need to input user name and login.
  - Create a deploy.sh script on the server. It will live in $HOME/bin/deploy.sh
  - That script looks in $HOME/lz for the cmb.tar.gz file. If it's there we untar to root, then remove the file from $HOME/lz
  - Added crontab to run $HOME/deploy.sh every minute. Log to $HOME/log/cmb.log. If the file is not there, do not log anything.

Clunky... but it works.

Client Side deploy.sh
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

        TARGET=192.168.6.176
        tar czvf /tmp/cmb.tar.gz /var/vroot
        scp /tmp/cmb.tar.gz $TARGET:lz/.

Client Side deploy.sh
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

        #!/bin/sh
        FILE="/home/rgeorgia/lz/cmb.tar.gz"
        LOG="/home/rgeorgia/logs/cmb.log"

        if [ -f "$FILE" ]; then
            echo "[$(date +'%y-%m-%d %H:%M')] ${FILE} found" >> $LOG
            doas tar xzvf $FILE -C /  >/dev/null
            if [ $? -ne 0 ]; then
                echo "[$(date +'%y-%m-%d %H:%M')] Operation Failed, Exit Code: $?" >> $LOG
            else
                echo "[$(date +'%y-%m-%d %H:%M')] SUCCESS. Exit Code: $?" >> $LOG
                rm $FILE
                if [ $? -ne 0 ]; then
                    echo "[$(date +'%y-%m-%d %H:%M')] $FILE not removed: $?" >> $LOG
                else
                    echo "[$(date +'%y-%m-%d %H:%M')] $FILE removed: $?" >> $LOG
                fi
                            
            fi
        fi

References
----------

`Serve files securely on NetBSD over HTTPS via bozotic-httpd <https://www.unitedbsd.com/d/434-serve-files-securely-on-netbsd-over-https-via-bozotic-httpd>`_

