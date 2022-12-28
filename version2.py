import random
import time
from sense_emu import SenseHat



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


def scoreIncrease():
    global score
    global pause
    score += 1
    pause *= 0.95 # decrease pause by 5%
    sense.set_pixels(greenArrow)
    time.sleep(1)
    sense.clear()
    startJoyStickGame(lives, score, pause)

def scoreDecrease():
    global lives
    lives -= 1
    sense.set_pixels(redArrow)
    time.sleep(1)
    sense.clear()
    startJoyStickGame(lives, score, pause)
def upArrow(angle):
    if angle == 0:
       scoreIncrease()
    else:
        scoreDecrease()
def downArrow(angle):
    if angle == 180:
        scoreIncrease()
    else:
        scoreDecrease()
def leftArrow(angle):
    if angle == 270:
        scoreIncrease()
    else:
        scoreDecrease()
def rightArrow(angle):
    if angle == 90:
        scoreIncrease()
    else:
        scoreDecrease()

def gameOver(score):
    sense.set_rotation(0)
    sense.show_message("Game Over", text_colour=[255, 0, 0])
    sense.show_message("Score: " + str(score), text_colour=[255, 0, 0])
    time.sleep(1)
    sense.clear()

def detectOrientation():
    #gets the orientation of the sense hat and returns the angle back as the closest multiple of 90
    # Get the pitch, roll, and yaw angles in degrees
    orientation = sense.get_orientation_degrees()
    pitch = orientation['pitch']

    # Round the pitch angle to the closest multiple of 90
    pitch = round(pitch / 90) * 90
    return pitch

def startMotionGame():
    play = True
    while play == True:
        if lives > 0:
            setRandomOrientation()
            sense.set_pixels(whiteArrow)
            startTimer = time.time()
            detectInputs = True
            while detectInputs == True:
                if detectOrientation() == angle:
                    scoreIncrease()
                    detectInputs = False
                elif time.time() - startTimer > pause:
                    detectInputs = False
                    scoreDecrease()
        else:
            gameOver(score)
            play = False
            break

def startJoyStickGame(lives, score, pause):
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
            detectInputs = True
            while detectInputs == True:
                for event in sense.stick.get_events():
                    if event.action == "pressed":
                        if event.direction == "up":
                            upArrow(angle)
                            detectInputs = False
                        elif event.direction == "down":
                            downArrow(angle)
                            detectInputs = False
                        elif event.direction == "left":
                            leftArrow(angle)
                            detectInputs = False
                        elif event.direction == "right":
                            rightArrow(angle)
                            detectInputs = False
                        elif event.direction == "middle":
                            gameOver(score)
                            detectInputs = False
                    elif event.action == "held":
                        if event.direction == "middle":
                            gameOver(score)
                            detectInputs = False
                if time.time() - startTimer > pause:
                    detectInputs = False
                    scoreDecrease()


        else:
            gameOver(score)
            play = False
            break

def programStart():
    sense.clear()
    sense.show_message("Press joystick to start or shake for motion control", text_colour=[255, 255, 255])

    while True:
        events = sense.stick.get_events()
        for event in events:
            if event.action == "pressed":
                startJoyStickGame(lives, score, pause)
            else:
                continue
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1 or y > 1 or z > 1:
            startMotionGame()

        else:
            pass

programStart()











