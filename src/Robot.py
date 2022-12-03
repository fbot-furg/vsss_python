from enum import Enum
from select import select
import string
from Communication import Communication

class Team(Enum):
    YELLOW = 1
    BLUE = 2
#não sei usar o Enum


class Robot:
    def __init__(self, id = int, team = string):
        self.id = id
        self.team = team

        self._communication = Communication()

    def _Robot(self):
        if self.team == True:
            return self._communication.yellow_robot(self.id)
        else:
            return self._communication.blue_robot(self.id)

    def x(self):
        return self._Robot()[0]

    def y(self):
        return self._Robot()[1]
        
    def orient(self):
        return self._Robot()[2]

