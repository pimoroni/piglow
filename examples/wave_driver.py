#!/usr/bin/env python

"""
An interface for creating custom waves on the PiGlow.
"""

import math
from itertools import tee
from time import sleep
from sys import exit

try:
    import numpy
except ImportError:
    exit("This library requires the numpy module\nInstall with: sudo pip install numpy")

import piglow


# organised by rings (inner ring first)
LEDS = [
    [6, 12, 18],
    [5, 11, 17],
    [4, 10, 16],
    [3, 9, 15],
    [2, 8, 14],
    [1, 7, 13],
]


def wave(led_max=150, frame_delay=0.02, frame_count=None, initial_brightness=None, direction=None):
    """
    Creates a wave effect through the PiGlow board.

    Args (all are optional):
        led_max (int): the LED brightness at the peak of the wave.
        frame_delay (float): the time between each transition.
        frame_count (int): the number of transitions in a single wave.
        initial_brightness (int): the current brightness of the LEDs.
        direction (string): either 'inward' or 'outward'.
    """
    if initial_brightness is None:
        initial_brightness = min(piglow.get())

    if direction is None:
        direction = 'outward'

    if frame_count is None:
        frame_count = len(LEDS)

    if direction == 'outward':
        LEDS.reverse()

    led_set_count = len(LEDS)

    # initialise all of the LEDs
    piglow.all(initial_brightness)
    piglow.show()

    wave = _create_led_sine_wave(led_max, frame_count, initial_brightness, led_set_count)

    for wave_point in _window(wave, led_set_count):
        for i, led_set in enumerate(LEDS):
            for led in led_set:
                piglow.led(led, int(wave_point[i]))

            piglow.show()
            sleep(frame_delay)


def _create_led_sine_wave(led_max, frame_count, initial_brightness, led_set_count):
    """
    Creates a custom sine wave for a set of LEDs.

    Args:
        led_max (int): the brightest an LED can go.
        frame_count (int): the wave length.
        initial_brightness (int): the current brightness of the LEDs.
        led_set_count (int): the number of sets the wave passes through.

    Returns a numpy `array` containing the entire sine wave.
    """
    # create a generic sine wave that starts at -1
    peak = numpy.linspace(-math.radians(90), math.radians(270), frame_count)

    # adjust the amplitude to suite the range of our LED brightness
    peak = numpy.sin(peak) * led_max / 2 + led_max / 2

    # finally, we calibrate the wave troughs
    peak[peak < initial_brightness] = initial_brightness

    # create a beginning and end for the wave to occupy
    buffer = numpy.linspace(initial_brightness, initial_brightness, led_set_count)

    # Boom, we have our wave!
    return numpy.concatenate([buffer, peak, buffer])


def _window(iterable, size=3):
    """
    Generate a sequence of `sliding windows` over an iterable.

    >>> list(_window(range(5)))
    [(0, 1, 2), (1, 2, 3), (2, 3, 4)]
    """
    iters = tee(iterable, size)

    for i in range(1, size):
        for each in iters[i:]:
            next(each, None)

    return zip(*iters)

if __name__ == '__main__':
    wave()
