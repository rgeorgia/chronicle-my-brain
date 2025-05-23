Configure X1 Carbon
===================

Change consoles font. Added to rc.conf

.. code-block:: console

    # use terminus-b32 font on console
    allscreens_flags="-f terminus-b32"

.. code-block:: console
 	
    pw groupmod video -m rgeorgia || pw groupmod wheel -m rgeorgia

Used for LCD control, suspend, etc...

Update ``/boot/loader.conf``

.. code-block:: console

        # Thinkpad stuff
        acpi_video_load="YES"
        acpi_ibm_load="YES"


References:

- https://www.sacredheartsc.com/blog/freebsd-14-on-the-desktop/

- `Installing FreeBSD on a Lenovo Carbon X1 Gen6 <https://www.jrgsystems.com/posts/2020-10-21-installing-freebsd-on-lenovo-x1-carbon-thinkpad>`_
- `FreeBSD on X1 Carbon (Gen 6) <https://things.bleu255.com/runyourown/FreeBSD_on_X1_Carbon_(Gen_6)>`_

