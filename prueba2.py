import random
import sys
import matplotlib.pyplot as plt
import math
import numpy as np
x1 = 2
x2 = 5
x3 = -3
x4 = 0
y1 = 3
y2 = 5
y3 = -1
y4 = 0

a = [x1,y1]
b = [x2,y2]
c = [x3,y3]
d = [x4,y4]

print("el punto a es: ", a)
print("el punto b es: ", b)
print("el punto c es: ", c)
print("el punto d es: ", d)
class punto:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

    def cuadrante(cuadrante1,cuadrante2, cuadrante3, cuadrante4 ):
        if (x1>0)and (y1>0):
            print("a está en el primer cuadrante ")
        elif (x1<0)and (y1>0):
            print("a está en el segundo cuadrante ")
        elif (x1<0)and (y1<0):
            print("a está en el tercer cuadrante ")
        elif  (x1>0)and (y1<0):
            print("a está en el cuarto cuadrante ")
        elif  (x1==0)and (y1!=0):
            print("a está sobre el eje y ")
        elif  (x1!=0)and (y1==0):
            print("a está sobre el eje x ")
        elif  (x1==0)and (y1==0):
            print("a está en el origen de coordenadas ")   
        if (x3>0)and (y3>0):
            print("c está en el primer cuadrante ")
        elif (x3<0)and (y3>0):
            print("c está en el segundo cuadrante ")
        elif (x3<0)and (y3<0):
            print("c está en el tercer cuadrante ")
        elif  (x3>0)and (y3<0):
            print("c está en el cuarto cuadrante ")
        elif  (x3==0)and (y3!=0):
            print("c está sobre el eje y ")
        elif  (x3!=0)and (y3==0):
            print("c está sobre el eje x ")
        elif  (x3==0)and (y3==0):
            print("c está en el origen de coordenadas ")  
        if (x4>0)and (y4>0):
            print("d está en el primer cuadrante ")
        elif (x4<0)and (y4>0):
            print("d está en el segundo cuadrante ")
        elif (x4<0)and (y4<0):
            print("d está en el tercer cuadrante ")
        elif  (x4>0)and (y4<0):
            print("d está en el cuarto cuadrante ")
        elif  (x4==0)and (y4!=0):
            print("d está sobre el eje y ")
        elif  (x4!=0)and (y4==0):
            print("d está sobre el eje x ")
        elif  (x4==0)and (y4==0):
            print("d está en el origen de coordenadas ")      
            return

    def vector():
        VectorAB = [x2-x1,y2-y1]
        print("el vector AB es: ", VectorAB)
        ax = plt.axes()
        ax.arrow(x1,y1, x2,y2 , head_width=0.5, head_length=0.5)
        plt.ylim(-10,10)
        plt.xlim(-10,10)
        #plt.show()
        VectorBA = [x1-x2,y1-y2]
        print("el vector BA es: ", VectorBA)
        ax = plt.axes()
        ax.arrow(x2,y2, x1,y1 , head_width=0.5, head_length=0.5)
        plt.ylim(-10,10)
        plt.xlim(-10,10)
        #plt.show()
        return

    def distancia():
        d = math.sqrt((x2-x1)**2+(y2-y1)**2)
        print("la distancia AB es igual que BA y es:  ",d)
        return
print(punto.cuadrante("cuadrante1","cuadrante2","cuadrante3", "cuadrante4"))
print(punto.vector())
print(punto.distancia())


class Rectangulo:
    def __init__():
        


