import random
from sense_hat import SenseHat
sense = SenseHat()

sense.clear()

w = (255, 255, 255)
o = (0, 0, 0)

arrow = [
    o, o, o, w, w, o, o, o,
    o, o, w, w, w, w, o, o,
    o, w, o, w, w, o, w, o,
    w, o, o, w, w, o, o, w,
    o, o, o, w, w, o, o, o,
    o, o, o, w, w, o, o, o,
    o, o, o, w, w, o, o, o,
    o, o, o, w, w, o, o, o
]


sense.set_pixels(arrow)
