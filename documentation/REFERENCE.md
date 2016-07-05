#Piglow Function Reference

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
