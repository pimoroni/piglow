import time

import piglow


piglow.auto_update = True

print("Testing continuous set...")
piglow.set(0, [100, 100, 100])
time.sleep(1)
piglow.all(0)

print("Testing list/list set...")
piglow.set([0, 2, 4, 6, 8, 10, 12, 14, 16], [100, 100, 100, 100, 100, 100, 100, 100, 100])
time.sleep(1)
piglow.all(0)

print("Testing single value, multi LED set...")
piglow.set([1, 3, 5, 7, 9, 11, 13, 15, 17], 100)
time.sleep(1)
piglow.all(0)
