import random
import time
from sense_hat import SenseHat



sense = SenseHat()

sense.clear()


angle = 0

w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
o = (0, 0, 0)

whiteArrow = [
        o, o, o, w, w, o, o, o,
        o, o, w, w, w, w, o, o,
        o, w, o, w, w, o, w, o,
        w, o, o, w, w, o, o, w,
        o, o, o, w, w, o, o, o,
        o, o, o, w, w, o, o, o,
        o, o, o, w, w, o, o, o,
        o, o, o, w, w, o, o, o
    ]

redArrow = [
    o, o, o, r, r, o, o, o,
    o, o, r, r, r, r, o, o,
    o, r, o, r, r, o, r, o,
    r, o, o, r, r, o, o, r,
    o, o, o, r, r, o, o, o,
    o, o, o, r, r, o, o, o,
    o, o, o, r, r, o, o, o,
    o, o, o, r, r, o, o, o
    ]
greenArrow = [
    o, o, o, g, g, o, o, o,
    o, o, g, g, g, g, o, o,
    o, g, o, g, g, o, g, o,
    g, o, o, g, g, o, o, g,
    o, o, o, g, g, o, o, o,
    o, o, o, g, g, o, o, o,
    o, o, o, g, g, o, o, o,
    o, o, o, g, g, o, o, o
    ]

def setRandomOrientation():
    global angle
    angle = random.choice([0, 90, 180, 270])
    sense.set_rotation(angle)
    return angle

pause = 3 #initial time between turns

score = 0
angle = 0

play = True

def stickDirection():
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'up':
                return 'up'
            elif event.direction == 'down':
                return 'down'
            elif event.direction == 'left':
                return 'left'
            elif event.direction == 'right':
                return 'right'
            elif event.direction == 'middle':
                return 'middle'
            else:
                return 'none'


def angleFromStickDirection(stickDirection):
    if stickDirection == 'up':
        return 0
    elif stickDirection == 'right':
        return 90
    elif stickDirection == 'down':
        return 180
    elif stickDirection == 'left':
        return 270
    else:
        return 'none'

while play == True:
    
    

   sense.set_pixels(whiteArrow)
   time.sleep(pause)
   if setRandomOrientation() == angle or angleFromStickDirection(stickDirection()) == angle:
       sense.set_pixels(greenArrow)
       score += 1
       pause -= 0.1
   
   else:
        sense.set_pixels(redArrow)
        pause += 0.1
        play = False

sense.show_message("Game Over, you scored: " + score, text_colour = (255, 0, 0))
