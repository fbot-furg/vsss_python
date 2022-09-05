import imp
from Bezier import Bezier
import numpy as np
import sys
sys.path.insert(0, '/home/murilo/Documentos/fbot-vss-python/src/')
import FIRALib
import time
import MotionLib
import math

###########################
from numpy import array as a
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
####################################
fig = plt.figure(dpi=128)
traves = [[-0.740,-0.170],[-0.740,0.170],[0.740,-0.150],[0.740,0.170]]

carro = FIRALib.yellow_car(0)
bola = FIRALib.ball()

diff_x = bola[0] - traves[3][0]
diff_y = bola[1] - traves[3][1]


t_points = np.arange(0, 1, 0.01) #................................. Creates an iterable list from 0 to 1.
test = np.array([[carro[0], carro[1]], [diff_x+bola[0],diff_y+bola[1]], [bola[0], bola[1]]]) #.... Creates an array of coordinates.
test_set_1 = Bezier.Curve(t_points, test) #......................... Returns an array of coordinates.
tamanho = len(test_set_1)

"""
# PLOTA O GRAFICO DA CURVA
#####################################################################################
plt.subplot(2, 3, 3)
plt.xticks([i1 for i1 in range(-20, 20)]), plt.yticks([i1 for i1 in range(-20, 20)])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(b=True, which='major', axis='both')

plt.plot(test_set_1[:, 0], test_set_1[:, 1])
plt.plot(test[:, 0], test[:, 1], 'ro:')

print("Ponto",diff_x+bola[0],diff_y+bola[1],"Bola",bola[0],bola[1])
plt.show()
#####################################################################################
"""
contador = 0
while contador < tamanho:
    
    posi = test_set_1[contador]
    MotionLib.move_to(0, True, posi[0], posi[1])
    contador += 11

FIRALib.move(0,True,500000,500000)
time.sleep(0.75)
FIRALib.move(0,True,0,0)

