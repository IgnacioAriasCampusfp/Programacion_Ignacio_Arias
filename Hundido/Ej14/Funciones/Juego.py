import numpy as np
from colorama import Fore as fr
from Funciones import Guardar



def JuegoPro(posicionb1, posicionb2, posicionb3,tablerosinresolver,tablero):
        
        intentos = 0
        barcoshundidos = 0
        barco1vivo = True
        barco2vivo = True
        barco3vivo  = True
        
        """
        if all(tablero[posicionb1[:, 0], posicionb1[:, 1]] == 0) and all(tablero[posicionb2[:, 0], posicionb2[:, 1]] == 0) and all(tablero[posicionb3[:, 0], posicionb3[:, 1]] == 0):
            barco1()  # Colocar barco 1
            barco2()  # Colocar barco 2
            barco3()  # Colocar barco 3
"""
        
        while True:
            print(fr.RED + "Tablero \n",tablerosinresolver , fr.RESET)
            
            print(posicionb1+1)
            print(posicionb2+1)
            print(posicionb3+1)
            filaj = int(input("¿Qué fila quieres atacar? (o 111 para menú) "))
            if filaj == 111:
                eleccion = int(input("Menú \n1. Guardar\n2. Salir\n"))
                if eleccion == 1:
                    Guardar.guardar_partida(tablero,posicionb1,posicionb2,posicionb3)
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