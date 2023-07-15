import math
from vsss_client import Team
from classes.robot import Robot
from classes.ball import Ball

robot = Robot(Team.BLUE, 0)
ball = Ball()
kp = 5

def round_angle(angle):
    if angle > math.pi:
        angle -= 2 * math.pi
    elif angle < -math.pi:
        angle += 2 * math.pi
    return angle

while True:
    diff_x = ball.x() - robot.x()
    diff_y = ball.y() - robot.y()
    speed = 10
    foward = True

    target_angle = math.atan2(diff_y, diff_x)

    error_angle = round_angle(target_angle - robot.orientation())
    reverse_error_angle = round_angle(target_angle - robot.reverse_orientation())

    if abs(error_angle) > abs(reverse_error_angle):
        foward = False
        error_angle = reverse_error_angle

    error_angle *= kp

    if not foward:
        speed = -speed

    dist_point = math.sqrt(diff_x**2 + diff_y**2)

    wheels_speed = [0,0]
    if dist_point > 0.1:
        wheels_speed[0] = speed - error_angle
        wheels_speed[1] = speed + error_angle

    robot.set_speed(wheels_speed[0], wheels_speed[1])
    robot.move()

