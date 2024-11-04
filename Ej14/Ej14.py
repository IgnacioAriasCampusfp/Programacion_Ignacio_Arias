import numpy as np
from colorama import Fore as fr

tablero = np.zeros((20,20))
tablerosinresolver = np.zeros((20,20))
barcoshundidos = 0

posicionb1 = np.array([[0, 0], [0, 0]])
posicionb2 = np.array([[0, 0], [0, 0], [0, 0]])
posicionb3 = np.array([[0, 0], [0, 0], [0, 0], [0, 0]])

def cargar_partida():
    global tablero, posicionb1, posicionb2, posicionb3
    tablero = np.zeros((20, 20), dtype=int)  # Reiniciar el tablero por si acaso
    try:
        with open("partida_comenzada.txt", "r") as archivo:
            for i in range(20):
                fila = list(map(int, archivo.readline().strip().split()))
                if len(fila) != 20:
                    raise ValueError(f"La fila {i+1} no tiene 20 elementos.")
                tablero[i] = np.array(fila)  # Convertir la fila en un array de numpy
                posicionb1 = np.array(list(map(int, archivo.readline().strip().split())))
                posicionb2 = np.array(list(map(int, archivo.readline().strip().split())))
                posicionb3 = np.array(list(map(int, archivo.readline().strip().split())))
        print("Partida cargada.")
    except FileNotFoundError:
        print("No hay partida guardada. Generando nueva partida.")
    except ValueError as e:
        print(f"Error al cargar la partida: {e}")
        
        
def guardar_partida():
    with open("partida_comenzada.txt", "w") as archivo:
        for fila in tablero:
            archivo.write(" ".join(map(str, fila)) + "\n")
    print("Partida guardada.")

def JuegoPro():
        
        intentos = 0
        barcoshundidos = 0
        barco1vivo = True
        barco2vivo = True
        barco3vivo  = True
        
        if all(tablero[posicionb1[:, 0], posicionb1[:, 1]] == 0) and all(tablero[posicionb2[:, 0], posicionb2[:, 1]] == 0) and all(tablero[posicionb3[:, 0], posicionb3[:, 1]] == 0):
            barco1()
            barco2()
            barco3()
        global posicionb1, posicionb2, posicionb3
        while True:
            print(fr.RED + "Tablero \n",tablerosinresolver , fr.RESET)
            
            print(posicionb1+1)
            print(posicionb2+1)
            print(posicionb3+1)
            filaj = int(input("¿Qué fila quieres atacar? (o 111 para menú) "))
            if filaj == 111:
                eleccion = int(input("Menú \n1. Guardar\n2. Salir\n"))
                if eleccion == 1:
                    guardar_partida()
                    continue
                elif eleccion == 2:
                    break
            columnaj = int(input("¿Que columna quieres atacar?"))
            
            #Usando Case
            match tablero[filaj-1,columnaj-1]:
                case 2:
                    print("Ya has probado esa posición")
                    
                case 0:
                    print("Agua")
                    tablerosinresolver[filaj-1,columnaj-1] = 2
                    tablero[filaj-1,columnaj-1] = 2
                    intentos = intentos + 1
                case 1:
                    tablerosinresolver[filaj-1,columnaj-1] = 2
                    tablero[filaj-1,columnaj-1] = 2
                    print(fr.YELLOW + "Tocado" + fr.RESET)
                    
                    if all(tablerosinresolver[posicionb1[:, 0], posicionb1[:, 1]] == 2) and barco1vivo == True:
                        print(fr.GREEN+ "Has hundido el barco de dos columnas" + fr.RESET)
                        barcoshundidos = barcoshundidos + 1
                        barco1vivo = False
                        print(barcoshundidos)
                        continue
                    elif all(tablerosinresolver[posicionb2[:, 0], posicionb2[:, 1]]== 2) and barco2vivo == True:
                        print(fr.GREEN+"Has hundido el barco de tres columnas"+ fr.RESET)
                        barcoshundidos = barcoshundidos + 1
                        barco2vivo = False
                        print(barcoshundidos)
                        continue
                    elif all(tablerosinresolver[posicionb3[:, 0], posicionb3[:, 1]]== 2) and barco3vivo == True:
                        print(fr.GREEN+"Has hundido el barco de cuatro columnas"+ fr.RESET)
                        barcoshundidos = barcoshundidos + 1
                        barco3vivo = False
                        print(barcoshundidos)
                        continue
                    if barcoshundidos == 3:
                        print(barcoshundidos)
                        print("has ganado")
                        open("partida_comenzada.txt", "w").close()
                        break
           
            
                    
                    
                
                    
                    
                
                
                
                
                
def barco1():
    print("Colocar barco 1 de 2 de longitud")
    fila = np.random.randint(1,20)
    columna = np.random.randint(1,20)
    tablero[fila,columna] = 1
    global posicionb1
    
    direccion = np.random.randint(1,4)
    match direccion:
        case 1:
            tablero[fila,columna-1] = 1
            posicionb1 = np.array([[fila, columna], [fila, columna-1]])
            
        case 2:
            tablero[fila,columna+1] = 1
            posicionb1 = np.array([[fila, columna], [fila, columna+1]])
            
        case 3:
            tablero[fila+1,columna] = 1
            posicionb1 = np.array([[fila, columna], [fila + 1, columna]])
            
        case 4:
            tablero[fila-1,columna] = 1
            posicionb1 = np.array([[fila, columna], [fila - 1, columna]])
            
    
    
    
def barco2():
    print("Colocar barco 1 de 3 de longitud")
    global posicionb2
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
                break
        elif direccion == 2:  
            if columna <= 16 and tablero[fila, columna] == 0 and tablero[fila, columna + 1] == 0 and tablero[fila, columna + 2] == 0:
                tablero[fila, columna] = 1
                tablero[fila, columna + 1] = 1
                tablero[fila, columna + 2] = 1
                posicionb2 = np.array([[fila, columna], [fila, columna + 1], [fila, columna + 2]])
                break
        elif direccion == 3:  
            if fila <= 16 and tablero[fila, columna] == 0 and tablero[fila + 1, columna] == 0 and tablero[fila + 2, columna] == 0:
                tablero[fila, columna] = 1
                tablero[fila + 1, columna] = 1
                tablero[fila + 2, columna] = 1
                posicionb2 = np.array([[fila, columna], [fila + 1, columna], [fila + 2, columna]])
                break
        elif direccion == 4:  
            if fila >= 2 and tablero[fila, columna] == 0 and tablero[fila - 1, columna] == 0 and tablero[fila - 2, columna] == 0:
                tablero[fila, columna] = 1
                tablero[fila - 1, columna] = 1
                tablero[fila - 2, columna] = 1
                posicionb2 = np.array([[fila, columna], [fila - 1, columna], [fila - 2, columna]])
                break
            
        
def barco3():
    print("Colocar barco 3 de 4 de longitud")
    global posicionb3

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
                break

        elif direccion == 2:  
            if columna <= 16 and np.all(tablero[fila, columna:columna + 4] == 0): 
                tablero[fila, columna] = 1
                tablero[fila, columna + 1] = 1
                tablero[fila, columna + 2] = 1
                tablero[fila, columna + 3] = 1
                posicionb3 = np.array([[fila, columna], [fila, columna + 1], [fila, columna + 2], [fila, columna + 3]])
                break

        elif direccion == 3:  
            if fila <= 16 and np.all(tablero[fila: fila + 4, columna] == 0):
                tablero[fila, columna] = 1
                tablero[fila + 1, columna] = 1
                tablero[fila + 2, columna] = 1
                tablero[fila + 3, columna] = 1
                posicionb3 = np.array([[fila, columna], [fila + 1, columna], [fila + 2, columna], [fila + 3, columna]])
                break

        elif direccion == 4:  
            if fila >= 3 and np.all(tablero[fila - 3: fila + 1, columna] == 0): 
                tablero[fila, columna] = 1
                tablero[fila - 1, columna] = 1
                tablero[fila - 2, columna] = 1
                tablero[fila - 3, columna] = 1
                posicionb3 = np.array([[fila, columna], [fila - 1, columna], [fila - 2, columna], [fila - 3, columna]])
                break


cargar_partida()
barco1()
barco2()
barco3()
JuegoPro()