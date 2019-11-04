#!/usr/bin/env python

from piglow import tween

for _ in range(3):
    tween(2.0, [255] * 18)
    tween(2.0, [0] * 18)

for _ in range(3):
    tween(2.0, start=[0] * 18, end=[255] * 18)
    tween(2.0, start=[255] * 18, end=[0] * 18)
