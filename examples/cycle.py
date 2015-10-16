#!/usr/bin/env python

import time
import piglow

i = 0

while True:
    print(i)
    piglow.all(0)
    piglow.set(i % 18, [15, 31, 63, 127, 255, 127, 63, 31, 15])
    piglow.show()
    i += 1
    time.sleep(0.1)
