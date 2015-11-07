#!/usr/bin/env python

import time
import piglow

while True:
    for x in range(100):
        piglow.leg_bar(0, x / 100.0)
        piglow.leg_bar(1, x / 100.0)
        piglow.leg_bar(2, x / 100.0)
        piglow.white(0)
        piglow.show()
        time.sleep(0.01)
    for x in reversed(range(100)):
        piglow.leg_bar(0, x / 100.0)
        piglow.leg_bar(1, x / 100.0)
        piglow.leg_bar(2, x / 100.0)
        piglow.white(0)
        piglow.show()
        time.sleep(0.01)
