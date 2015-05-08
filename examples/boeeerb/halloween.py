#!/usr/bin/env python
##################################################
## Switch only yellow, orange and red to random ##
## brightness                                   ##
## Example by tng - @TommyBobbins               ##
##################################################

import piglow

piglow.auto_update = True

from time import sleep
import random

# Maximum random sleep between switching an LED on or off
sleep_period = 0.001

# Switch off all the lights first
piglow.all(0)

# We only want to select the Red, Orange and Yellow LEDs (roy)
roy_leds = [ "01","02","03", "07", "08", "09", "13","14", "15" ]

def random_brightness():
    sleep(random.uniform(0,sleep_period))
    return random.randint(0,255)

while True:
    # Switch one random roy LED to one random brightness
    led_to_switch = int(random.choice(roy_leds))
    piglow.led(led_to_switch, random_brightness())
    # Switch one random roy LED off 
    led_to_switch = int(random.choice(roy_leds))
    piglow.led(led_to_switch, 0)
