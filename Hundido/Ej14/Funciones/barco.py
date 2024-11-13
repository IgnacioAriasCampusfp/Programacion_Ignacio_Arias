import numpy as np


def barco1(tablero,posicionb1):
    print("Colocar barco 1 de 2 de longitud")
    fila = np.random.randint(1,20)
    columna = np.random.randint(1,20)
    tablero[fila,columna] = 1
    
    
    direccion = np.random.randint(1,4)
    try:
        match direccion:
            case 1:
                tablero[fila,columna-1] = 1
                posicionb1 = np.array([[fila, columna], [fila, columna-1]])
                return posicionb1
                
            case 2:
                tablero[fila,columna+1] = 1
                posicionb1 = np.array([[fila, columna], [fila, columna+1]])
                return posicionb1
                
            case 3:
                tablero[fila+1,columna] = 1
                posicionb1 = np.array([[fila, columna], [fila + 1, columna]])
                return posicionb1
                
            case 4:
                tablero[fila-1,columna] = 1
                posicionb1 = np.array([[fila, columna], [fila - 1, columna]])
                return posicionb1
    except ValueError:
        barco1()
  
def barco2(tablero,posicionb2):
    print("Colocar barco 1 de 3 de longitud")
    
    while True:
        fila = np.random.randint(0, 20)  
        columna = np.random.randint(0, 20) 
        direccion = np.random.randint(1, 5)  

        if direccion == 1:  
            if columna >= 2 and tablero[fila, columna] == 0 and tablero[fila, columna - 1] == 0 and tablero[fila, columna - 2] == 0:
                tablero[fila, columna] = 1
                tablero[fila, columna - 1] = 1
                tablero[fila, columna - 2] = 1
                posicionb2 = np.array([[fila, columna], [fila, columna - 1], [fila, columna - 2]])
                return posicionb2
        elif direccion == 2:  
            if columna <= 16 and tablero[fila, columna] == 0 and tablero[fila, columna + 1] == 0 and tablero[fila, columna + 2] == 0:
                tablero[fila, columna] = 1
                tablero[fila, columna + 1] = 1
                tablero[fila, columna + 2] = 1
                posicionb2 = np.array([[fila, columna], [fila, columna + 1], [fila, columna + 2]])
                return posicionb2
        elif direccion == 3:  
            if fila <= 16 and tablero[fila, columna] == 0 and tablero[fila + 1, columna] == 0 and tablero[fila + 2, columna] == 0:
                tablero[fila, columna] = 1
                tablero[fila + 1, columna] = 1
                tablero[fila + 2, columna] = 1
                posicionb2 = np.array([[fila, columna], [fila + 1, columna], [fila + 2, columna]])
                return posicionb2
        elif direccion == 4:  
            if fila >= 2 and tablero[fila, columna] == 0 and tablero[fila - 1, columna] == 0 and tablero[fila - 2, columna] == 0:
                tablero[fila, columna] = 1
                tablero[fila - 1, columna] = 1
                tablero[fila - 2, columna] = 1
                posicionb2 = np.array([[fila, columna], [fila - 1, columna], [fila - 2, columna]])
                return posicionb2
                
        
            
        
def barco3(tablero,posicionb3):
    print("Colocar barco 3 de 4 de longitud")


    while True:
        fila = np.random.randint(0, 20)  
        columna = np.random.randint(0, 20) 
        direccion = np.random.randint(1, 5)

        if direccion == 1:  
            if columna >= 3 and np.all(tablero[fila, columna-3:columna+1] == 0):  
                tablero[fila, columna] = 1
                tablero[fila, columna - 1] = 1
                tablero[fila, columna - 2] = 1
                tablero[fila, columna - 3] = 1
                posicionb3 = np.array([[fila, columna], [fila, columna - 1], [fila, columna - 2], [fila, columna - 3]])
                return posicionb3

        elif direccion == 2:  
            if columna <= 16 and np.all(tablero[fila, columna:columna + 4] == 0): 
                tablero[fila, columna] = 1
                tablero[fila, columna + 1] = 1
                tablero[fila, columna + 2] = 1
                tablero[fila, columna + 3] = 1
                posicionb3 = np.array([[fila, columna], [fila, columna + 1], [fila, columna + 2], [fila, columna + 3]])
                return posicionb3

        elif direccion == 3:  
            if fila <= 16 and np.all(tablero[fila: fila + 4, columna] == 0):
                tablero[fila, columna] = 1
                tablero[fila + 1, columna] = 1
                tablero[fila + 2, columna] = 1
                tablero[fila + 3, columna] = 1
                posicionb3 = np.array([[fila, columna], [fila + 1, columna], [fila + 2, columna], [fila + 3, columna]])
                return posicionb3

        elif direccion == 4:  
            if fila >= 3 and np.all(tablero[fila - 3: fila + 1, columna] == 0): 
                tablero[fila, columna] = 1
                tablero[fila - 1, columna] = 1
                tablero[fila - 2, columna] = 1
                tablero[fila - 3, columna] = 1
                posicionb3 = np.array([[fila, columna], [fila - 1, columna], [fila - 2, columna], [fila - 3, columna]])
                return posicionb3
        