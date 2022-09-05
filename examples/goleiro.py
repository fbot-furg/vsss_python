import sys
sys.path.insert(0, '/home/murilo/Documentos/fbot-vss-python/src/')
import FIRALib
import MotionLib

while True:
    ball = FIRALib.ball()
    car = FIRALib.yellow_car(0)
    if(car[0]<0.615 or car[0]> 0.750):
        MotionLib.move_to(0,True,0.615,0)
    else:
        FIRALib.move(0,True,0,0)

        if(car[2] > 1.38):
            if(car[1] > 0.250):
                FIRALib.move(0,True,-10,-10)  
            elif(car[1]< -0.250):
                FIRALib.move(0,True,10,10)       

            else:      

                if(ball[1]-0.02 < car[1] < ball[1]+0.02):
                    FIRALib.move(0,True,0,0)
                        
                else:
                    if(car[1] < ball[1]):
                        FIRALib.move(0,True,50,50)
                    else:
                        FIRALib.move(0,True,-50,-50)       

        else:
            FIRALib.move(0,True,0,5)
            
 






