from Robot import Robot
from Communication import Communication
import math

class go_to:
    def __init__(self, id, team, val_x, val_y, orie) -> None:
        self.id = id
        self.team = team
        self.val_x = val_x
        self.val_y = val_y
        self.orie = orie
        self.car = Robot(id, team)
        
        car_x = self.car.x()
        car_y = self.car.y()

        self.diff_x = self.val_x - car_x
        self.diff_y = self.val_y - car_y

        self.comm = Communication()

    def __theta(self):
        return math.atan(self.diff_y/self.diff_x)


    def __dist(self):
        return math.sqrt( self.diff_x * self.diff_x + self.diff_y * self.diff_y)

    
    def __err_orientation(self):
        return ( self.__theta()- self.orie)

    def go_to(self):
        robot_speed = 20
        orientation_kp = 20
        if self.__dist() < 0.1:
            self.comm.move(self.id, self.team, 0,0)
        else:
            velocidade = self.__err_orientation * orientation_kp

            if self.x > 0.0:
                self.comm.move(self.id, self.team, -velocidade + robot_speed, velocidade + robot_speed)
            else:
                self.comm.move(self.id, self.team, -velocidade - robot_speed, velocidade - robot_speed)


while True:
    go = go_to(0, True, 0, 0, 0)
    go.go_to()
