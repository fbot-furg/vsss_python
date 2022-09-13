from enum import Enum
from .Communication import Communication

class Team(Enum):
    YELLOW = 1
    BLUE = 2
    
class Robot:
    
    _communication = None
    
    def __init__(self, _id: int, team: Team) -> None:
        self.id = _id
        self.team = team
        
        self._communication = Communication()
        
    def _robot(self):
        if self.team == Team.YELLOW:
            return self._communication.yellow_robot(self.id)
        else:
            return self._communication.blue_robot(self.id)
        
    def x(self):
        return self._robot().x
    
    def y(self):
        return self._robot().y
    
    def orientation(self):
        return self._robot().orientation
    
    # remover futuramente: usado para teste de singleton
    def environment(self):
        return self._communication.environment()

    # remover futuramente: usado para teste de singleton
    def stop(self):
        self._communication.stop()
    
        
        
        
    