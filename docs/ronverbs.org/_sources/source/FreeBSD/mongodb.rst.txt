Adventures with FreeBSD and Mongodb
====================================

pkg search mongodb
installed mongodb80
got a post install message to install npm and mongosh

Mongodb Post Install Message
-----------------------------

.. code-block:: bash

        Message from mongodb80-8.0.12_2:

        --
        MongoDB on Raspberry Pi can work but is unsupported upstream.
        Please read https://jira.mongodb.org/browse/SERVER-71772 and enable option
        ARMV80A if you run this on a non-LSE ARM cpu like Raspberry Pi 4.

        MongoDB 6.0 and up do not include the 'mongo' CLI shell anymore. You can
        use the MongoDB Shell (https://github.com/mongodb-js/mongosh).
        # pkg install npm
        $ npm install mongosh
        $ npx mongosh mongodb://127.0.0.1:27017/

I don't really like nodejs and my trust level for npm is very low. If using mongodb becomes impossible without mongosh, I will rethink, but until then... nope.


