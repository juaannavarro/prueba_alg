import random
import sys
import matplotlib.pyplot as plt
import math
import numpy as np
ejeXpos=10
ejeXneg=-10
ejeYpos=10
ejeYneg=-10
x1= random.randint(-10,10)
y1 = random.randint(-10,10)
while True:
            print("quieres elegir una coordenada X?")
            print("1.si")
            print("2.no")
            print()
            eleccion = int(input("Cuál es tu elección?: "))
            break 
        
if eleccion == 1:
    x=int(input("Elige una coordenada para X: "))
    if (x >= ejeXneg) and  (x <= ejeXpos):
        print("la coordenada X es ", x)
    else:
        print("error")
        

elif eleccion == 2:
        x= 0
        print("la coordenada X es ", x)

else:
    print("vuelve a elegir ")

while True:
            print("quieres elegir una coordenada Y?")
            print("1.si")
            print("2.no")
            print()
            eleccion = int(input("Cuál es tu elección?: "))
            break 
        
if eleccion == 1:
        y=int(input("Elige una coordenada para Y: "))
        if (y >= ejeXneg) and  (y <= ejeXpos):
                print("la coordenada X es ", y)
        else:
            print("error")
                
elif eleccion == 2:
    y= 0
    print("la coordenada Y es ", y)
else:
    print("vuelve a elegir ")
            

formato = [x,y]
print("el punto es ", formato)

class punto:

    def __init__(self, X, Y):
        self.X=X
        self.Y=Y
    def cuadrante(cuadrante1,cuadrante2, cuadrante3, cuadrante4 ):
        if (x>=0)and (y>=0):
            print("es el primer cuadrante ")
        elif (x<=0)and (y>=0):
            print("es el segundo cuadrante ")
        elif (x<=0)and (y<=0):
            print("es el tercer cuadrante ")
        elif  (x>=0)and (y<=0):
            print("es el cuarto cuadrante ")
        elif  (x==0)and (y!=0):
            print("esta sobre el eje y ")
        elif  (x!=0)and (y==0):
            print("esta sobre el eje x ")
        elif  (x==0)and (y==0):
            print("es el origen de coordenadas ")       
            return


    def vector():
        azar = [x1,y1]
        print("el punto aleatorio es ", azar)
        Vector = [x1-x,y1-y]
        print("el vector entre los dos puntos es ", Vector)
        ax = plt.axes()
        ax.arrow(x,y, x1,y1 , head_width=0.5, head_length=0.5)
        plt.ylim(-10,10)
        plt.xlim(-10,10)
        #plt.show()
        return

    def distancia():
        azar = [x1,y1]
        print("el punto aleatorio es ", azar)  
        d = math.sqrt((x1-x)**2+(y1-y)**2)
        print("la d es ",d)
        return
        

print(punto.cuadrante("cuadrante1","cuadrante2","cuadrante3", "cuadrante4"))
print(punto.vector())
print(punto.distancia())




 