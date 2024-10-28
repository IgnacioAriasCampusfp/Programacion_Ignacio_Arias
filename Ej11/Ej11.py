import numpy as np

tablero = np.zeros((5,5))
tablerosinresolver = np.zeros((5,5))

fila = np.random.randint(1,5)
columna = np.random.randint(1,5)
tablero[fila,columna] = 1

def Juego():
    intentos = 0

    while True:
        print("Tablero \n",tablerosinresolver)
        filaj = int(input("¿Que fila quieres atacar?"))
        columnaj = int(input("¿Que columna quieres atacar?"))
        if tablero[filaj-1,columnaj-1] == 1:
            print(f"¡Has hundido el barco! \n Has necesitado {intentos} intentos")
            print(tablero)
            break
        elif  tablerosinresolver[filaj-1,columnaj-1] == -1:
            print("Ya has probado esa posición")
        else:
            print("Agua")
            tablerosinresolver[filaj-1,columnaj-1] = -1
            intentos = intentos + 1
    
        
Juego()