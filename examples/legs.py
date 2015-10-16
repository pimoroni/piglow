#!/usr/bin/env python

import time
import piglow

i = 0
x = 0

while True:
    if i % 32 == 0:
        piglow.leg((x % 3), 64)
        x += 1
    piglow.set(0, map(lambda x: x - 1 if x > 1 else 0, piglow.get()))
    piglow.show()
    time.sleep(0.001)
    i += 1
