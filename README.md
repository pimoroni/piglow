PiGlow sample code and instructions
===================================

PiGlow is a small add on board for the Raspberry Pi that provides 18 individually controllable LEDs. You can use it for all sorts of things! And of course, it fits inside a Pibow!

Setting up your Raspberry Pi
----------------------------

PiGlow is based on an IC that communicates via i2c protocol. We need to enable i2c communication on your Raspberry Pi for it to work.

Enable the i2c driver modules by editing the modules config file:

    sudo nano /etc/modules

Then either add or ensure the following lines are at the end of the file:

    i2c-dev
    i2c-bcm2708

You may also need to ensure the driver modules are not blacklisted by editing the blacklist config file:

    sudo nano /etc/modprobe.d/raspi-blacklist.conf

Ensure that if the following two lines exist in that config file that you comment them out by adding a # sign at the start of the line. So:

    blacklist spi-bcm2708
    blacklist i2c-bcm2708

...should become...

    # blacklist spi-bcm2708
    # blacklist i2c-bcm2708

Then we install the i2c libraries and Python support:

    sudo apt-get install python-smbus

Then reboot your Pi!
