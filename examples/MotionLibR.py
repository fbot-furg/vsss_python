import imp
import sys
sys.path.insert(0, '/home/murilo/Documentos/fbot-vss-python/src/')
import FIRALib
import math
from Velocity import Velocity
import Redis

def move_to(id, Team, x,y):
    robot_speed = 20
    orientation_kp = 20

    while True:
        ########################################################
        ball = Redis.ball()
        if Team == True:
            car = Redis.yellow_car(id)
        else:
            car = Redis.blue_car(id)
        ########################################################

        car_x = car[0]
        car_y = car[1]

        diff_x = x - car_x
        diff_y = y - car_y

        theta = math.atan(diff_y/diff_x)
        dist = math.sqrt(diff_x*diff_x + diff_y*diff_y)
        err_orientation = (theta - car[2])
        velocidade = err_orientation * 10

        if dist < 0.0625:
            break
        else:
            
            velocidade = err_orientation * orientation_kp

            if diff_x > 0.0:
                FIRALib.move(id,Team, -velocidade + robot_speed, velocidade + robot_speed)
            else:
                FIRALib.move(id,Team, -velocidade - robot_speed, velocidade - robot_speed)
 


def follow_ball(id, Team):
    robot_speed = 5
    orientation_kp = 5

    while True:
        ########################################################
        ball = Redis.ball()
        if Team == True:
            car = Redis.yellow_car(id)
        else:
            car = Redis.blue_car(id)
        ########################################################

        car_x = car[0]
        car_y = car[1]

        x = ball[0] 
        y = ball[1] 

        diff_x = x - car_x
        diff_y = y - car_y

        theta = math.atan(diff_y/diff_x)
        dist = math.sqrt(diff_x*diff_x + diff_y*diff_y)
        err_orientation = (theta - car[2])
        velocidade = err_orientation * 10

        if dist < 0.1:
            FIRALib.move(id,Team, 0, 0)
        else:
            
            velocidade = err_orientation * orientation_kp

            if diff_x > 0.0:
                FIRALib.move(id,Team, -velocidade + robot_speed, velocidade + robot_speed)
            else:
                FIRALib.move(id,Team, -velocidade - robot_speed, velocidade - robot_speed)
