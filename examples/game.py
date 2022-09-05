import MotionLib
from multiprocessing import Process
import goleiro
from shoot import shoot


if __name__ == '__main__':
    print("START")
    while True:
        seguibola_b1 = Process(target= MotionLib.follow_ball,args=(0,False))
        seguibola_b1.start()
        seguibola_b2 = Process(target= MotionLib.follow_ball,args=(1,False))
        seguibola_b2.start()
        seguibola_b3 = Process(target= MotionLib.follow_ball,args=(2,False))
        seguibola_b3.start()
        seguibola_y1 = Process(target= MotionLib.follow_ball,args=(0,True))
        seguibola_y1.start()
        seguibola_y2 = Process(target= MotionLib.follow_ball,args=(1,True))
        seguibola_y2.start()
        seguibola_y3 = Process(target= MotionLib.follow_ball,args=(2,True))
        seguibola_y3.start()
        print("END")



