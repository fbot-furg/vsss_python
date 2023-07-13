import math
from vsss_client import Team
from classes.robot import Robot
from classes.ball import Ball

robot = Robot(Team.BLUE, 0)
ball = Ball()
kp = 5
spedd = 10

while True:
    diff_x = ball.x() - robot.x()
    diff_y = ball.y() - robot.y()
    target_angle = math.atan2(diff_y, diff_x)

    error_angle = (target_angle - robot.orientation()) * kp

    dist_point = math.sqrt(diff_x**2 + diff_y**2)

    wheels_speed = [0,0]
    if dist_point > 0.1:
        wheels_speed[0] = spedd - error_angle
        wheels_speed[1] = spedd + error_angle

    robot.set_speed(wheels_speed[0], wheels_speed[1])
    robot.move()

