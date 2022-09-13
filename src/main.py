import time

from classes.Communication import Communication
from classes.Robot import Robot, Team

comm = Communication()

time.sleep(0.5)
print(comm.environment())

goalie = Robot(0, Team.BLUE)
time.sleep(0.5)

print(comm.environment())
print(goalie.environment())

comm.stop()
goalie.stop()