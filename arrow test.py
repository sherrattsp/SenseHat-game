import random
from sense_hat import SenseHat
sense = SenseHat()
import time




countdown = 5
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
incrementsPerMilisecond = 255 / (1000 / countdown) #increments being how many times per milisecond to increase the red value by
timePerIncrement = round((countdown / 255), 3)
redValue = 0
i = 0




while i < 255:
    redValue += 1
    o = (redValue, 0, 0)
    sense.set_pixels(arrow)
    time.sleep(timePerIncrement)
    i +=1





