from vsss_client import FIRASim, Team, Command

class Robot:
    def __init__(self, team: Team, id: int) :
        self.fira = FIRASim("config.ini")

        self.id = id
        self.team = team
        self.wheel_left = 0
        self.wheel_right = 0

    def x(self):
        return self.fira.robot(self.team, self.id).x

    def y(self):
        return self.fira.robot(self.team, self.id).y
    
    def orientation(self):
        return self.fira.robot(self.team, self.id).orientation

    def set_speed(self, x, y):
        self.wheel_left = x
        self.wheel_right = y

    def move(self):
        cmd = Command(self.team, self.id, self.wheel_left, self.wheel_right)
        self.fira.send_command([cmd])
