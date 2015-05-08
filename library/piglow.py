import sn3218, atexit

sn3218.enable()
sn3218.enable_leds(0b111111111111111111)

clear_on_exit = True
auto_update = False

legs = [
  # r   o   y   g   b   w
  [ 6,  7,  8,  5,  4,  9 ],
  [ 17, 16, 15, 13, 11, 10 ],
  [ 0,  1,  2,  3,  14, 12 ]
]

values = [0] * 18

colours = {
  "red"    : 0,
  "orange" : 1,
  "yellow" : 2,
  "green"  : 3,
  "blue"   : 4,
  "white"  : 5
}

white  = lambda v: ring(5,v)
blue   = lambda v: ring(4,v)
green  = lambda v: ring(3,v)
yellow = lambda v: ring(2,v)
orange = lambda v: ring(1,v)
red    = lambda v: ring(0,v)

arm1   = lambda v: arm(0,v)
arm2   = lambda v: arm(1,v)
arm3   = lambda v: arm(2,v)

led1   = lambda v: set(0,v)
led2   = lambda v: set(1,v)
led3   = lambda v: set(2,v)
led4   = lambda v: set(3,v)
led5   = lambda v: set(4,v)
led6   = lambda v: set(5,v)
led7   = lambda v: set(6,v)
led8   = lambda v: set(7,v)
led9   = lambda v: set(8,v)
led10  = lambda v: set(9,v)
led11  = lambda v: set(10,v)
led12  = lambda v: set(11,v)
led13  = lambda v: set(12,v)
led14  = lambda v: set(13,v)
led15  = lambda v: set(14,v)
led16  = lambda v: set(15,v)
led17  = lambda v: set(16,v)
led18  = lambda v: set(17,v)			

arm    = lambda x,y: leg(x - 1 if auto_update else x,y)
spoke  = lambda x,y: leg(x - 1 if auto_update else x,y)

def show():
  '''
  Output the contents of the values list to PiGlow.
  '''
  sn3218.output(values)

def set(leds, value):
  '''
  Set one or more LEDs with one or more values

  Args:
  * leds - A single index, or list of indexes of the LEDs to set
  * values - A single value, or list of values to set
  '''
  global values
  if isinstance(leds, list):
    for led in leds:
      if isinstance(value, list):
        values[leds[led] % 18] = (value[led] % 256)
      else:
        values[led % 18] = (value % 256)
  elif isinstance(leds, int):
    leds = leds % 18
    if isinstance(value, list):
      values[leds:leds + len(value)] = map(lambda v: v % 256, value)
      if len(values) > 18:
        wrap = values[18:]
        values = values[:18]
        set(0, wrap)
    else:
      values[leds] = (value % 256)
  else:
    raise ValueError("Invalid LED/LEDs")
  if auto_update:
    show()

def ring(ring, value):
  '''
  Set the brightness of a specific ring
  '''
  ring = ring % 7
  set([legs[0][ring], legs[1][ring], legs[2][ring]], value)

def leg_bar(leg, percentage):
  # 1530 = 6 * 255
  amount = int(1530.0 * percentage)
  for led in reversed(legs[leg]):
    set(led,255 if amount > 255 else amount)
    amount = 0 if amount < 255 else amount - 255

def leg(leg, intensity):
  set(legs[leg % 3], intensity)

def led(led, intensity):
  if auto_update:
    led = led - 1
  set(led, intensity)

def single(leg, ring, intensity):
  set(legs[leg % 3][ring % 7], intensity)

def colour(colour, intensity):
  if not isinstance(colour, int):
    if colour in colours:
      colour = colours[colour]
      ring(colour, intensity)
      return True
    else:
      raise ValueError("Invalid Colour")
      return False
  ring(colour-1, intensity)
  return True
	
def all(value):
  set(0, [value]*18)

def clear():
  set(0, [0]*18)

def off():
  all(0)
  show()

def _exit():
  if clear_on_exit:
    off()

atexit.register(_exit)
