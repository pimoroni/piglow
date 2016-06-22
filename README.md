![Piglow](piglow-logo.jpg)

The PiGlow is a small add on board for the Raspberry Pi that provides 18 individually controllable LEDs.

Learn more: https://shop.pimoroni.com/products/piglow

This repository contains the library and examples for the PiGlow board.

## Easy Install

Just run our installer. To do this fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window, run our easy installer by typing:

```bash
curl -sS get.pimoroni.com/piglow | bash
```

This script will install the library and copy the examples in this repository to `~/Pimoroni/piglow`

## Backwards Compatibility

The PiGlow Python library is designed to support examples written for Jason's PiGlow library found here: https://github.com/Boeeerb/PiGlow

It's compatible with the examples, and we've ported some over to show you how it's done.

## Using PiGlow

To use the piglow library, you'll probably want to start by importing it:

```python
import piglow
```

Now, you can turn some LEDs on:

```python
piglow.red(64)
```

Nothing will happen yet, you've got to update PiGlow with your changes. Why? Because it's quicker! If you're setting up a pattern it costs time and resources to redraw every step of that setup to the PiGlow, so we don't do that. Instead you need to call `show` like so:

```python
piglow.show()
```

A bug is a feature you can't turn off, however, so if you want to change that behaviour you can set it after importing piglow:

```python
piglow.auto_update = True
```

This will turn on auto update, refreshing the PiGlow after each change so you don't have to.

##Function Reference

### Settings
* `auto_update` - Set to True or False, determines if the PiGlow should automatically update after each LED change
* `clear_on_exit` - Set to True or False, determines if the PiGlow should be cleared on exit

### Colours
* `white( value from 0 to 255 )`
* `blue( value from 0 to 255 )`
* `green( value from 0 to 255 )`
* `yellow( value from 0 to 255 )`
* `orange( value from 0 to 255 )`
* `red( value from 0 to 255 )`

### Arm, Spoke, Leg, they're all the same thing!

`arm( index from 0 to 2, value from 0 to 255 )`

### Multiple LEDs in various different ways

The `set` method accepts a list of LEDs, a list of values, or a single LED or value, or any permutation therein:

`set(0, 255)` - sets LED 0 to full brightness

`set([1,3,5,7,9,11,13,15,17],255)` - sets all odd LEDs to full brightness

`set(0,[50,50,50])` - let the 3 LEDs starting at index 0 to 50 brightness

##Other support for PiGlow

**Gordon Henderson** (@drogon on Twitter) has very kindly added support for PiGlow into his very popular wiringPi library and even includes a basic command line tool that you can use to control your PiGlow! http://wiringpi.com/dev-lib/piglow/

**Simon Walters** (@cymplecy) has added awesome PiGlow support to his Raspberry Pi GPIO Scratch library: http://cymplecy.wordpress.com/2013/08/12/scratch-gpio-piglow-support/

**Jason Barnett** has put together a great Python class and a load of samples: https://github.com/Boeeerb/PiGlow

**Ben Lebherz** has forked Jasons project and tidied up the code a bit while adding gamma correction: https://github.com/benleb/PyGlow

**Manuel Ernst** has created a Node.js library: https://github.com/zaphod1984/node-piglow

##More information

For more information the datasheet for the SN3218 IC is included in this repository which outlines the complete communication protocol for the chip.

For those wanting to wire up their PiGlow in other ways these are the GPIO pins used by the module:

- P1 & P17 (3V3)
- P2 (5V)
- P14 (GND)
- P3 (SDA)
- P5 (SCL)

##Special Thanks

A special thanks for Jason Barnett for carrying the PiGlow torch with his original library.
