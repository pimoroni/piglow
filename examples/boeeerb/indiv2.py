#!/usr/bin/env python
##################################################
## Switch each colour on in sequence on and off ##
##                                              ##
## Example by Jason - @Boeeerb                  ##
##################################################

import piglow
from time import sleep

piglow.auto_update = True

val = 20
colour = 1

while True:
    if colour == 19:
        colour = 1
        if val == 20:
            val = 0
        else:
            val = 20

    piglow.led(colour, val)
    sleep(0.2)

    colour = colour + 1
