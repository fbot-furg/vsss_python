from Robot import Robot
from Communication import Communication
import math

class potential_field:
    def __init__(self, id, team, val_x, val_y, orie) -> None:
        self.id = id
        self.team = team
        self.val_x = val_x
        self.val_y = val_y
        self.orie = orie
        self.car = Robot(id, team)

        self.car_x = self.car.x()
        self.car_y = self.car.y()
        self.diff_x = self.val_x - self.car_x
        self.diff_y = self.val_y - self.car_y

        self.comm = Communication()

    def __theta(self):
        return math.atan(self.diff_y/self.diff_x)


    def __dist(self):
        return math.sqrt( self.diff_x * self.diff_x + self.diff_y * self.diff_y)

    
    def __err_orientation(self):
        return self.__theta() - self.car.orient()

################################################POTENTIAL########################################################
    def __enemies(self):
        if self.team == True:
            return False
        else:
            return True

    def __enemies_position(self):
        enemie_team = self.__enemies()

        enemie_0 = Robot(0,enemie_team)
        enemie_1 = Robot(1,enemie_team)
        enemie_2 = Robot(2,enemie_team)
        

        return [(enemie_0.x(), enemie_0.y()), (enemie_1.x(), enemie_1.y()), (enemie_2.x(), enemie_2.y())]

    def __modulo(self, position):
        position_x = position[0]
        position_y = position[1]

        diff_x = position_x - self.car_x
        diff_y = position_y - self.car_y
        return math.sqrt(diff_x * diff_x + diff_y * diff_y)


    def __modulos(self, positions):
        modulo_0 = self.__modulo(positions[0])
        modulo_1 = self.__modulo(positions[1])
        modulo_2 = self.__modulo(positions[2])
        
        return [modulo_0, modulo_1, modulo_2]

    def __deviation(self, car, modulo):
        enimies = self.__enemies_position()
        enimies = enimies[car]

        diff_x = enimies[1] - self.car_x

        if diff_x > 0.0:
            return ([1,3])

        else:
            return ([3,1])

    def potential(self):
        car = -1
        positions = self.__enemies_position()
        modulos = self.__modulos(positions)
        for modulo in modulos:
            car += 1
            if modulo < 0.35:
                return self.__deviation(car, modulo)
            else:
                return [1,1]

####################################################################################################################

    def go_to(self):
        robot_speed = 20
        orientation_kp = 20
        potential = self.potential()
        potential_1 = potential[0]
        potential_2 = potential[1]
        if self.__dist() < 0.1:
            self.comm.move(self.id, self.team, 0,0)
        else:
            velocidade = self.__err_orientation() * orientation_kp
            if self.diff_x > 0.0:
                self.comm.move(self.id, self.team, (-velocidade + robot_speed)*potential_1, (velocidade + robot_speed)*potential_2)
            else:
                self.comm.move(self.id, self.team, (-velocidade - robot_speed)*potential_1, (velocidade - robot_speed)*potential_2)



