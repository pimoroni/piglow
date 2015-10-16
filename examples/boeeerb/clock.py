#!/usr/bin/env python
######################################
## A binary clock using the PiGlow  ##
##                                  ##
##  Example by Jason - @Boeeerb     ##
######################################

import piglow
from time import sleep
from datetime import datetime

piglow.auto_update = True

### You can customise these settings ###

show12hr = 1  # Show 12 or 24hr clock - 0= 24hr, 1= 12hr
ledbrightness = 10  # Set brightness of LED - 1-255 (recommend 10-20, put 0 and you won't see it!)
hourflash = 1  # Choose how to flash change of hour - 1= white leds, 2= all flash

armtop = "s"  # h= hour, m= minutes, s= seconds
armright = "m"
armbottom = "h"

### End of customising ###

piglow.all(0)

hourcount = 0
hourcurrent = 0

while True:
    time = datetime.now().time()
    print(str(time))
    hour = time.hour
    min = time.minute
    sec = time.second

    if show12hr == 1:
        if hour > 12:
            hour = hour - 12

    # Check if current hour is different and set ready to flash hour
    if hourcurrent != hour:
        hourcount = hour
        hourcurrent = hour

    if armbottom == "h":
        arm3 = hour
    elif armbottom == "m":
        arm3 = min
    else:
        arm3 = sec

    for x in range(6):
        piglow.led(13 + x, (arm3 & (1 << x)) * ledbrightness)

    if armright == "h":
        arm2 = hour
    elif armright == "m":
        arm2 = min
    else:
        arm2 = sec

    for x in range(6):
        piglow.led(7 + x, (arm2 & (1 << x)) * ledbrightness)

    if armtop == "h":
        arm1 = hour
    elif armtop == "m":
        arm1 = min
    else:
        arm1 = sec

    for x in range(6):
        piglow.led(1 + x, (arm1 & (1 << x)) * ledbrightness)

    # Flash the white leds for the hour
    if hourcount != 0:
        sleep(0.5)
        if hourflash == 1:
            piglow.white(ledbrightness)
        if hourflash == 2:
            piglow.all(ledbrightness)
        sleep(0.5)
        hourcount = hourcount - 1
    else:
        sleep(0.1)
