import random
import time
from sense_hat import SenseHat



sense = SenseHat()

sense.clear()




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

pause = 3 #initial time between turns

score = 0
angle = 0
lives = 3

play = True


def checkInput():
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                if angle == 0:
                    return True
                else:
                    return False
            if event.direction == "right":
                if angle == 90:
                    return True
                else:
                    return False
            if event.direction == "down":
                if angle == 180:
                    return True
                else:
                    return False
            if event.direction == "left":
                if angle == 270:
                    return True
                else:
                    return False
            if event.direction == "middle":
                return False

def gameOver():
    sense.show_message("Game Over", text_colour=[255, 0, 0])
    sense.show_message("Score: " + str(score), text_colour=[255, 0, 0])
    time.sleep(1)
    sense.clear()

def startGame(lives, score):
    play = True
    while play == True:

        '''
        check if lives remain
        set random orientation
        show arrow in specified orientation
        start timer
        wait for input
        if input is correct, add 1 to score if in specified time
        '''

        if lives > 0:
            setRandomOrientation()
            sense.set_pixels(whiteArrow)
            startTimer = time.time()
            checkInput()
        else:
            gameOver()
            play = False
            break
        if checkInput() == True and time.time() - startTimer < pause:
                score += 1
                sense.set_pixels(greenArrow)
                time.sleep(1)
                sense.clear()
        else:
            lives -= 1
            sense.set_pixels(redArrow)
            time.sleep(1)
            sense.clear()


sense.show_message("Press joystick to start", text_colour=[255, 0, 0])
sense.stick.wait_for_event()
startGame(lives, score)








