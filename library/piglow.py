from __future__ import division

import atexit
import operator
import time
from sys import exit


__version__ = '1.2.5'

_is_setup = False
clear_on_exit = True
auto_update = False

_legs = [
    # r   o   y   g   b   w
    [6, 7, 8, 5, 4, 9],
    [17, 16, 15, 13, 11, 10],
    [0, 1, 2, 3, 14, 12]
]

_map = _legs[0] + _legs[1] + _legs[2]

_values = [0] * 18

colours = {
    "red": 0,
    "orange": 1,
    "yellow": 2,
    "green": 3,
    "blue": 4,
    "white": 5
}


def white(v): ring(5, v)


def blue(v): ring(4, v)


def green(v): ring(3, v)


def yellow(v): ring(2, v)


def orange(v): ring(1, v)


def red(v): ring(0, v)


def arm1(v): arm(0, v)


def arm2(v): arm(1, v)


def arm3(v): arm(2, v)


def led1(v): set(0, v)


def led2(v): set(1, v)


def led3(v): set(2, v)


def led4(v): set(3, v)


def led5(v): set(4, v)


def led6(v): set(5, v)


def led7(v): set(6, v)


def led8(v): set(7, v)


def led9(v): set(8, v)


def led10(v): set(9, v)


def led11(v): set(10, v)


def led12(v): set(11, v)


def led13(v): set(12, v)


def led14(v): set(13, v)


def led15(v): set(14, v)


def led16(v): set(15, v)


def led17(v): set(16, v)


def led18(v): set(17, v)


def arm(x, y): leg(x - 1, y)


def spoke(x, y): leg(x - 1, y)


def show():
    """Output the contents of the values list to PiGlow."""

    setup()
    sn3218.output(_values)


def get():
    return _values


def set(leds, value):
    """Set one or more LEDs with one or more values.

    You can set multiple LEDs with the same value, or supply a list of LEDs and values.

    :param led: A single index, or list of indexes of the LEDs to set
    :param value: A single value, or list of values to set"""

    if isinstance(value, list) and isinstance(leds, int):
        offset = leds
        leds = [(offset + x) % 18 for x in range(len(value))]
    if isinstance(leds, list):
        leds = [_map[l] for l in leds]
    elif isinstance(leds, int):
        leds = _map[leds]
    _set(leds, value)


def _set(leds, value):
    global _values

    if isinstance(leds, list):
        if isinstance(value, list):
            for x in range(len(value)):
                _values[leds[x] % 18] = (value[x] % 256)
        else:
            for led_index in leds:
                _values[led_index % 18] = (value % 256)

    elif isinstance(leds, int):
        leds %= 18
        if isinstance(value, list):
            _values[leds:leds + len(value)] = map(lambda v: v % 256, value)
            if len(_values) > 18:
                wrap = _values[18:]
                _values = _values[:18]
                set(0, wrap)
        else:
            _values[leds] = (value % 256)
    else:
        raise ValueError("Invalid LED(s)")

    if auto_update:
        show()


def ring(ring_index, value):
    """Set the brightness of a specific ring"""

    ring_index %= 6
    _set([_legs[0][ring_index], _legs[1][ring_index], _legs[2][ring_index]], value)


def leg_bar(leg_index, percentage):
    """Display a bargraph on a leg.

    A leg/arm/spoke is the line of 6 LEDs the emanates from the center of Piglow to the edge.

    :param leg_index: leg from 0 to 2
    :param percentage: percentage to display in decimal

    """

    if percentage > 1.0 or percentage < 0:
        raise ValueError("percentage must be between 0.0 and 1.0")

    # 1530 = 6 * 255
    amount = int(1530.0 * percentage)
    for led_index in reversed(_legs[leg_index % 3]):
        _set(led_index, 255 if amount > 255 else amount)
        amount = 0 if amount < 255 else amount - 255


def leg(leg_index, intensity):
    _set(_legs[leg_index % 3], intensity)


def led(led_index, intensity):
    """Compatibility function for old PiGlow library
    Accepts LED between 1 and 18.
    Calls set(led - 1, intesity)

    :param led_index: LED number from 1 to 18
    :param intensity: brightness from 0 to 255

    """

    set(led_index - 1, intensity)


def single(leg_index, ring_index, intensity):
    """Sets a single LED by its leg/ring

    :param leg_index: leg index of LED
    :param ring_index: ring index of LED
    :param intensity: brightness from 0 to 255

    """

    _set(_legs[leg_index % 3][ring_index % 6], intensity)


def tween(duration, end, start=None):
    """Tweens to a particular set of intensities.
    Also accepts an optional starting point, otherwise
    the current state of the LED is used.

    :param duration: duration in seconds
    :param end: list of 18 values to tween to
    :param start: list of 18 values to start from

    """

    if not len(end) == 18:
        raise ValueError("Requires list of 18 values")

    fps = 1.0 / 60
    steps = int(duration / fps)

    if start is None:
        start = list(_values)

    deltas = map(operator.sub, end, start)
    deltas_per_frame = [d / steps for d in deltas]

    new = start
    for x in range(steps):
        new = list(map(operator.add, new, deltas_per_frame))
        new_ints = [int(round(n)) for n in new]
        _set(0, new_ints)
        # avoid double write
        if not auto_update:
            show()
        time.sleep(fps)


def colour(colour, intensity):
    """Set all LEDs of a particular colour to specified intensity

    :param colour: text name of LED colour; red, orange, yellow, green, blue, white
    :param intensity: brightness from 0 to 255

    """

    if not isinstance(colour, int):
        if colour in colours:
            ring(colours[colour], intensity)
            return True
        else:
            raise ValueError("Invalid Colour")
    ring(colour - 1, intensity)
    return True


def all(value):
    """Set all LEDs to a specific brightness"""

    global _values
    _values = [value] * 18

    if auto_update:
        show()


def clear():
    """Set all LEDS to 0/off"""

    all(0)


def off():
    """Set all LEDs to 0/off"""
    
    all(0)
    show()


def _exit():
    if clear_on_exit:
        off()


def setup():
    global _is_setup, sn3218

    if _is_setup:
        return True

    try:
        import sn3218
    except ImportError:
        raise ImportError("This library requires the sn3218 module\nInstall with: sudo pip install sn3218")

    sn3218.enable()
    sn3218.enable_leds(0b111111111111111111)

    atexit.register(_exit)

    _is_setup = True

