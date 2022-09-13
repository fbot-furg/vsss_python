#class Position has x y and orientation

class Position:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.orientation = 0
        
    def __str__(self) -> str:
        return "x: " + str(self.x) + " y: " + str(self.y) + " orientation: " + str(self.orientation)
