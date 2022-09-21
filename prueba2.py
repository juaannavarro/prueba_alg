import math
class Punto:
    def __init__(self, coordenada_X=0, coordenada_Y=0):
 
        self.coordenada_X = coordenada_X
        self.coordenada_Y = coordenada_Y
    def __str__(self):
        return  "({}, {})".format(self.coordenada_X, self.coordenada_Y)
 
    def cuadrante(self):
        if self.coordenada_X > 0 and self.coordenada_Y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.coordenada_X < 0 and self.coordenada_Y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.coordenada_X < 0 and self.coordenada_Y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.coordenada_X > 0 and self.coordenada_Y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.coordenada_X != 0 and self.coordenada_Y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.coordenada_X == 0 and self.coordenada_Y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))
 
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.coordenada_X - self.coordenada_X, p.coordenada_Y - self.coordenada_Y) )
 
    def distancia(self, p):
        d = math.sqrt ( (p.coordenada_X - self.coordenada_X)**2 + (p.coordenada_Y - self.coordenada_Y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(
            self, p, d))
 
class Rectangulo:
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
    
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura
 
    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )
 
    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ) )
 
    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ) )

 
 
 
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)
 
A.cuadrante()
C.cuadrante()
D.cuadrante()
 
A.vector(B)
B.vector(A)
 
 
 
A.distancia(B)
B.distancia(A)
 
A.distancia(D)
B.distancia(D)
C.distancia(D)
 
R = Rectangulo(A, B)
R.base()
R.altura()
R.area()       