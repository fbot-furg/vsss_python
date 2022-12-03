import sys
sys.path.insert(0,"/home/castanheira/v3s_ws/FIRA_Class/src")
from Communication import Communication
from potential_field import potential_field

while True:
    ball = Communication().ball()
    go = potential_field(0, True, ball.x, ball.y, 0)
    go.go_to()
