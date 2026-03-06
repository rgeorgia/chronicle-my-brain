openHammer and httpd
====================


Getting the web to my local machine
-----------------------------------

So, I wanted work on my ``chronicle-my-brain`` project with uses Sphinx to print. Normally I just open ``doc/index.html`` directly with Firefox; however, OpenBSD will not allow any file **not** located in ~/Downloads to be opened. I read and played with unveil for a couple of hours and made no progress. It was a total waste of time. I may need a Masters degree in CS before I can understand how the whole unveil thing works. I get the idea behind it, but no matter how I try or what I change, I can not alter the default behavior. So, I gave up.

I thought to myself, "Self? Why not just do a ``make gh-pages`` and build the files at /var/www/htdocs/chronicle-my-brain?" **Now** I have to figure out how to get httpd configured properly and running. If it's not one thing, it's another. Every Linux distro I've uses is so much easier. FreeBSD and NetBSD is also easier, but I am bent on making this work. Despite all it's user-unfriendly, non intuitive quirks, OpenBSD still seems like a good choice for me. Maybe, just before I expire, I'll have a slightly higher than noob understanding. Hopefully.

I enabled and started httpd without error. When I go to http://localhost I get redirected to http://localhost/cgi-bin/bgplg, which produces a 404 Not Found error. Guess I need to understand why it's redirecting to cgi and how to configure. I know it has something to do with /etc/httpd.conf. :)

This is a good article, `Self-hosting a static site with OpenBSD, httpd, and relayd <https://citizen428.net/blog/self-hosting-static-site-openbsd-httpd-relayd/>`_

I kept trying to do ``http://localhost``, but what I wanted is ``https://127.0.0.1`` Now that worked.

I modified /etc/httpd.conf

.. code-block:: bash

        types { include "/usr/share/misc/mime.types" }

        server "ronverbs.dev" {
            listen on * port 80
            root "/htdocs"
        }

        server "ronverbs.dev" {
            listen on 127.0.0.1 port 8080
            root "/htdocs/chronicle-my-brain"
        }


Now I modified my Makefile in the Sphynx project repo to the following

.. code-block:: bash

        .PHONY: gh-pages

        gh-pages:
            @sphinx-build ./docs ./docs/gh-pages

        prod-pages:
            doas rm -rf /var/www/htdocs/chronicle-my-brain
            doas /home/rgeorgia/.local/share/myvenv/cmb/bin/sphinx-build ./docs /var/www/htdocs/chronicle-my-brain

Now things are working.
