import random

ejeXpos=10
ejeXneg=-10
ejeYpos=10
ejeYneg=-10


class punto:
    def __init__(self, X, Y):
        self.X=X
        self.Y=Y

    def creacion_puntosX(seleccion, azar):
        while True:
            print("quieres elegir una coordenada X?")
            print("1.si")
            print("2.no")
            print()
            eleccion = int(input("Cuál es tu elección?: "))
            break 
        
        if eleccion == 1:
            seleccion=int(input("Elige una coordenada para X: "))
            if (seleccion >= ejeXneg) and  (seleccion <= ejeXpos):
                        print("la coordenada X es ", seleccion)
            else:
                return

        elif eleccion == 2:
            azar= random.randint(-10,10)
            print("la coordenada X es ", azar)

        else:
            print("vuelve a elegir ")
            return

    def creacion_puntosY(seleccion1, azar1):
        while True:
            print("quieres elegir una coordenada Y?")
            print("1.si")
            print("2.no")
            print()
            eleccion = int(input("Cuál es tu elección?: "))
            break 
        
        if eleccion == 1:
            seleccion1=int(input("Elige una coordenada para Y: "))
            if (seleccion1 >= ejeXneg) and  (seleccion1 <= ejeXpos):
                print("la coordenada X es ", seleccion1)
            else:
                return
        elif eleccion == 2:
            azar1= random.randint(-10,10)
            print("la coordenada Y es ", azar1)
        else:
            print("vuelve a elegir ")
            return


        print("el punto es: ",(seleccion or azar), (seleccion1 or azar1))

        x=seleccion
        y=seleccion1
        x2=azar
        y2=azar1
        s=repr(x)+repr(x2)+repr(y)+repr(y2)
        print(s) 
print(punto.creacion_puntosX("seleccion", "azar"))
print(punto.creacion_puntosY("seleccion1", "azar1"))
print(punto.creacion_puntosY("seleccion","azar","seleccion1", "azar1"))

