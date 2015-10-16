import piglow
import time

for x in range(18):
    piglow.led(x + 1, 100)
    piglow.show()
    time.sleep(0.5)
    piglow.led(x + 1, 0)
    piglow.show()
    time.sleep(0.5)
