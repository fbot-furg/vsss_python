from enum import Enum
from select import select
from Communication import Communication

class Team(Enum):
    YELLOW = 1
    BLUE = 2

class Robot:
    def __init__(self, id = int, team = Team):
        self.id = id
        self.team = team

        self._communication = Communication()

    def _Robot(self):
        if self.team == Team.YELLOW:
            return self._communication.yellow_robot(self.id)
        else:
            return self._communication.blue_robot(self.id)

    def x(self):
        return self._Robot()[0]

    def y(self):
        return self._Robot()[1]
    def orient(self):
        return self._Robot()[2]

