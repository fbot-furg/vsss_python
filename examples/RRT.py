import imp
import pygame
from RRTBasePy import RRTGraph
from RRTBasePy import RRTMap
import sys
sys.path.insert(0, '/home/murilo/Documentos/fbot-vss-python/src/')
import FIRALib
import MotionLib
import time

def main():
    ball = FIRALib.ball()
    yellow_car = FIRALib.yellow_car(0)
    yellow_car_x = 428+(yellow_car[0]/2)*1000
    yellow_car_y = 305 - (yellow_car[1]/2)*1000
    ball_x = 428+(ball[0]/2)*1000
    ball_y = 305 - (ball[1]/2)*1000
    #rint(ball_x, ball_y)  
    dimensions = (610,856) # (y,x)
    start = (yellow_car_x, yellow_car_y)     
    goal = (ball_x, ball_y)# (x,y)
    obsdim = 150
    obsnum = 3
    iteration=0
    #t1 = 0

    pygame.init()
    map = RRTMap(start,goal,dimensions, obsdim, obsnum)
    graph= RRTGraph(start,goal,dimensions, obsdim, obsnum)

    obstacles = graph.makeobs()
    map.drawMap(obstacles)

    while (not graph.path_to_goal()):

        if iteration % 10 == 0:
            X, Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad+2, 0)
            pygame.draw.line(map.map, map.blue, (X[-1],Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),map.edgeThinckness)

        else:
            X, Y, Parent = graph.expand()
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad+2, 0)
            pygame.draw.line(map.map, map.blue, (X[-1],Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),map.edgeThinckness)

        if iteration % 5 == 0:
            pygame.display.update()
        iteration += 1
    map.drawPath(graph.getPathCoords())
    
    pygame.display.update()
    pygame.event.clear()
    pontos = graph.getPathCoords()

    #print(pontos)
    tamanho = len(pontos)
    tamanho = tamanho -3
    print(tamanho)
    while (tamanho) >= 0:
        
        ponto = pontos[tamanho]
        MotionLib.move_to(0,True, ((-428+(ponto[0]))/1000)*2 , ((+305-(ponto[1]))/1000)*2)
        tamanho -= 1
    FIRALib.move(0,True,0,0)
##PARTE 2 NÂO TA PRONTA AINDA

if __name__ == '__main__':
    main()
       