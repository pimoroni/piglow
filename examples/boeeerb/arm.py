#!/usr/bin/env python
#########################################################
## Set each arm of the PiGlow to a specific brightness ##
##                                                     ##
##  Example by Jason - @Boeeerb                        ##
#########################################################

import piglow
from time import sleep

piglow.auto_update = True

piglow.all(0)

while True:
    piglow.arm(3,0)
    piglow.arm(1,20)
    sleep(0.5)
    piglow.arm(1,0)
    piglow.arm(2,20)
    sleep(0.5)
    piglow.arm(2,0)
    piglow.arm(3,20)
    sleep(0.5)

    piglow.all(0)
    piglow.arm1(10)
    sleep(0.5)
    piglow.all(0)
    piglow.arm2(10)
    sleep(0.5)
    piglow.all(0)
    piglow.arm3(10)
    sleep(0.5)
