import random

from sense_hat import sense_hat
from random import choice

sense = sense_hat()

# Global variables

direction = 'U'
lives = 3
noOfGmaes = 0


def correctOrientation():
    correctPitch = 270
    orientation = sense.get_orientation()
    pitch = orientation["pitch"]
    roll = orientation["roll"]
    yaw = orientation["yaw"]



def showArrow(direction):
    """
    Method will take a direction as a string (U, D, L & R) for up, down, left and right respectively



    """
    # the colours will be stored in variables, they will also be given an alias for ease of entering this into the matrix of pixels
    white = (255, 255, 255)
    w = white
    red = (255, 0, 0)
    r = red
    off = (0, 0, 0)
    o = off
    # using the set.pixels method a right, left, up and down arrow will need to be defined

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

    set_rotation()

    sense.set_pixels(arrow)


def set_rotation():
    angle = choice([0, 90, 180, 270])

    if angle == 0:
        sense.set_rotation(0)
        direction = 'U'
    elif angle == 90:
        sense.set_rotation(90)
        direction = 'R'
    elif angle == 180:
        sense.set_rotation(180)
        direction = 'D'
    elif angle == 270:
        sense.set_rotation(270)
        direction = 'L'


def countdown(time):
    #method to show a count-down based on a given time parameter
    numToShow = time
    i = 0
    while  i < time:
        sense.show_message(time - i, text_colour=getRandomColour(), back_colour=getRandomColour())
        i += 1


def getRandomColour():
    colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return colour

def getDirection():
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 0)
    y = round(y, 0)
def startGame(gameNo):


def startProgram():
    sense.show(lives + " lives remaining")
    countdown(3)
    noOfGames =+ 1
    




