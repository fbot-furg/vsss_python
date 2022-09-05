import imp
import numpy as np
import sys
sys.path.insert(0, '/home/murilo/Documentos/fbot-vss-python/src/')# perguntar depois pro caras
import FIRALib


def Velocity(id,ToF,Ve,Wa):
    ToF = ToF
    id = id
    L = 7.5
    R = 0.001

    V = Ve
    W = np.deg2rad(Wa)

    wr = ((2.0*V)+(W*L))/(2.0+R)
    wl = ((2.0*V)-(W*L))/(2.0+R)

    FIRALib.move(id,ToF,wl,wr)

def modulo(a):
    if a < 0:
        a = a * (-1)
    
    return(a)