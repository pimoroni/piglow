.. role:: python(code)
   :language: python

.. toctree::
   :titlesonly:
   :maxdepth: 0

Welcome
-------

This documentation will guide you through the methods available in the Piglow python library.

Piglow is a simple blinky LED add-on with 18 LEDs in 6 different colours.

* More information - https://shop.pimoroni.com/products/piglow
* GPIO Pinout - https://pinout.xyz/pinout/piglow
* Get the code - https://github.com/pimoroni/piglow
* Get help - http://forums.pimoroni.com/c/support

At A Glance
-----------

.. automoduleoutline:: piglow
   :members:

Set All LEDs
------------

.. automodule:: piglow
   :noindex:
   :members: all

Clear All LEDs
--------------

.. automodule:: piglow
   :noindex:
   :members: clear

Set One Colour
--------------

Each of Piglow's rings consists of a different LED colour, from inside-to-out:

White, Blue, Green, Yellow, Orange, Red.

You can also call the colour names as functions, eg: :python:`piglow.white(255)`

.. automodule:: piglow
   :noindex:
   :members: colour

Set A Single LED
----------------

.. automodule:: piglow
   :noindex:
   :members: led

LED Bargraph
------------

.. automodule:: piglow
   :noindex:
   :members: leg_bar

LED Bargraph
------------

.. automodule:: piglow
   :noindex:
   :members: leg_bar

Turn Off
--------

.. automodule:: piglow
   :noindex:
   :members: off

Set Ring
--------

.. automodule:: piglow
   :noindex:
   :members: ring

Set LEDs
--------

.. automodule:: piglow
   :noindex:
   :members: set

Show
----

.. automodule:: piglow
   :noindex:
   :members: show

Single by Leg/Ring
------------------

.. automodule:: piglow
   :noindex:
   :members: single

Tween
-----

.. automodule:: piglow
   :noindex:
   :members: tween
