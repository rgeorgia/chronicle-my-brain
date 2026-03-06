openHammer Printing
===================

Installed the following:

.. code-block:: bash

   pkg_add cups gutenprint foomatic-db splix hplip

And started the service

.. code-block:: bash

    rcctl enable cupsd
    rcctl start cupsd

I tried every which way, and installed the pdd file, but nothing worked. I finally installed using hplip and socket://<ip address>:9100>. That worked
