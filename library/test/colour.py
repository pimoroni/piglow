import time

import piglow


piglow.auto_update = True

for x in range(6):
    piglow.all(0)
    piglow.ring(x, 100)
    time.sleep(0.5)
