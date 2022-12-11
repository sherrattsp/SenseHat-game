import random

from sense_hat import sense_hat
from random import choice

sense = sense_hat()


sense.clear()
o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
