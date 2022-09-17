import socket
import sys

from protos.common_pb2 import Frame
sys.path.insert(0,"./protos")
from packet_pb2 import Environment, Packet
from command_pb2 import Commands, Command


class Communication:
    def __init__(self):
        
        self.LOCALHOST = "127.0.0.1"
        self.HOST = "224.0.0.1"
        self.VISION_ADDR = 10002
        self.COMMAND_ADDR = 20011

    
    def __receive(self):
        socket_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_receive.bind((self.HOST,self.VISION_ADDR))
        data, addr = socket_receive.recvfrom(2048) 
        return data

    def __environment(self):
        environment = Environment()
        environment.ParseFromString(self.__receive())
        return  environment.frame


    def ball(self):
        return self.__environment().ball
        

    def blue_team(self):
        return self.__environment().robots_blue

    def yellow_team(self):
        return self.__environment().robots_yellow

    def blue_robot(self, id):
        for robot in self.blue_team():
            if robot.robot_id == id:
                return([robot.x, robot.y, robot.orientation])
    
    def yellow_robot(self, id):
        for robot in self.yellow_team():
            if robot.robot_id == id:
                return([robot.x, robot.y, robot.orientation])



comn = Communication()
print(comn.blue_team())