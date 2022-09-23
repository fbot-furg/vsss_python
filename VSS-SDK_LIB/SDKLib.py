import socket
import sys
sys.path.insert(0,"./msg")
from state_pb2 import Pose, Ball_State, Robot_State, Global_State


host = "127.0.0.1"                  #endereços string
porta_recebe = 5555                #porta int  


socket_recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #declaro um socket
socket_recebe.connect((host, porta_recebe))# .bind(1 argumento) é usado para endereço local e .connect() para endereço remoto

data, addr = socket_recebe.recvfrom(1024)
globa = Global_State()
a = globa.ParseFromString(data)
print(a)