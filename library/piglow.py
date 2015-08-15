import sn3218
import atexit
import time

sn3218.enable()
sn3218.enable_leds(0b111111111111111111)        

clear_on_exit = True
auto_update = False

_legs = [
  # r   o   y   g   b   w
  [ 6,  7,  8,  5,  4,  9 ],
  [ 17, 16, 15, 13, 11, 10 ],
  [ 0,  1,  2,  3,  14, 12 ]
]

_map = _legs[0] + _legs[1] + _legs[2]

_values = [0] * 18

colours = {
  "red"    : 0,
  "orange" : 1,
  "yellow" : 2,
  "green"  : 3,
  "blue"   : 4,
  "white"  : 5
}

def white(v):  ring(5,v)
def blue(v):   ring(4,v)
def green(v):  ring(3,v)
def yellow(v): ring(2,v)
def orange(v): ring(1,v)
def red(v):    ring(0,v)

def arm1(v):   arm(0,v)
def arm2(v):   arm(1,v)
def arm3(v):   arm(2,v)

def led1(v):   set(0,v)
def led2(v):   set(1,v)
def led3(v):   set(2,v)
def led4(v):   set(3,v)
def led5(v):   set(4,v)
def led6(v):   set(5,v)
def led7(v):   set(6,v)
def led8(v):   set(7,v)
def led9(v):   set(8,v)
def led10(v):  set(9,v)
def led11(v):  set(10,v)
def led12(v):  set(11,v)
def led13(v):  set(12,v)
def led14(v):  set(13,v)
def led15(v):  set(14,v)
def led16(v):  set(15,v)
def led17(v):  set(16,v)
def led18(v):  set(17,v)			

def arm(x,y):   leg(x - 1,y)
def spoke(x,y): leg(x - 1,y)

def show():
    '''
    Output the contents of the values list to PiGlow.
    '''
    sn3218.output(_values)

def get():
    return _values

def set(leds, value):
    if isinstance(value, list) and isinstance(leds, int):
        offset = leds
        leds = [(offset+x)%18 for x in range(len(value))]
    if isinstance(leds, list):
        leds = [ _map[led] for led in leds ]
    elif isinstance(leds, int):
        leds = _map[leds]
    _set(leds, value)

def _set(leds, value):
    '''
    Set one or more LEDs with one or more values

    Args:
    * leds - A single index, or list of indexes of the LEDs to set
    * values - A single value, or list of values to set
    '''
    global _values

    if isinstance(leds, list):
        if isinstance(value, list):
            for x in range(len(value)):
                _values[leds[x] % 18] = (value[x] % 256)
        else:
            for led in leds:
                _values[led % 18] = (value % 256)

    elif isinstance(leds, int):
        leds = leds % 18
        if isinstance(value, list):
            _values[leds:leds + len(value)] = map(lambda v: v % 256, value)
            if len(_values) > 18:
                wrap = _values[18:]
                _values = _values[:18]
                set(0, wrap)
        else:
            _values[leds] = (value % 256)
    else:
        raise ValueError("Invalid LED(s)")
   
    if auto_update:
        show()

def ring(ring, value):
    '''
    Set the brightness of a specific ring
    '''
    ring = ring % 7
    _set([_legs[0][ring], _legs[1][ring], _legs[2][ring]], value)

def leg_bar(leg, percentage):
    # 1530 = 6 * 255
    amount = int(1530.0 * percentage)
    for led in reversed(_legs[leg]):
        _set(led,255 if amount > 255 else amount)
        amount = 0 if amount < 255 else amount - 255

def leg(leg, intensity):
    _set(_legs[leg % 3], intensity)

def led(led, intensity):
    '''Compatibility function for old PiGlow library
    Accepts LED between 1 and 18.
    Calls set(led - 1, intesity)

    Args:
    * led - LED number from 1 to 18
    * intensity - brightness from 0 to 255
    '''
    set(led - 1, intensity)

def single(leg, ring, intensity):
    '''Sets a single LED by its leg/ring
    Args:
    * leg - leg index of LED
    * ring - ring index of LED
    * intensity - brightness from 0 to 255
    '''
    _set(_legs[leg % 3][ring % 7], intensity)

def tween(duration, end, start = None):
    '''Tweens to a particular set of intensities.
    Also accepts an optional starting point, otherwise
    the current state of the LED is used.
    Args:
    * duration - duration in seconds
    * end - list of 18 values to tween to
    * start - list of 18 values to start from
    '''
    if not len(end) == 18:
        raise ValueError("Requires list of 18 values")

    fps = 1.0/60
    steps = int(duration / fps)

    if start is None:
        start = _values

    for x in range(steps):
        new = []
        for y in range(18):
            s = start[y]
            e = end[y]
            c = float(e - s)
            b = s + ((c/float(steps)) * (x+1))
            new.append(int(b))
        _set(0, new)
        show()
        time.sleep(fps)

def colour(colour, intensity):
    if not isinstance(colour, int):
        if colour in colours:
            ring(colours[colour], intensity)
            return True
        else:
            raise ValueError("Invalid Colour")
            return False
    ring(colour-1, intensity)
    return True
	
def all(value):
    global _values
    _values = [value]*18
    

def clear():
    all(0)

def off():
    all(0)
    show()

def _exit():
    if clear_on_exit:
        off()

atexit.register(_exit)
