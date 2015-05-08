#!/usr/bin/env python

import time, pimglow as piglow

i = 0
x = 0

while True:
  if i % 32 == 0:
    piglow.leg((x % 3), 64)
    x = x + 1
  piglow.values = map(lambda x: x - 1 if x > 1 else 0, piglow.values)
  piglow.show()
  time.sleep(0.001)
  i = i + 1
