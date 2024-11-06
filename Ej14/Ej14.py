import numpy as np
import sys
sys.path.append("Funciones")
#import Guardar

from Funciones import Cargar
from Funciones import barco
from Funciones import Juego


from colorama import Fore as fr

tablero = np.zeros((20,20), dtype=int)
tablerosinresolver = np.zeros((20,20), dtype=int)
barcoshundidos = 0

posicionb1 = np.array([[0, 0], [0, 0]])
posicionb2 = np.array([[0, 0], [0, 0], [0, 0]])
posicionb3 = np.array([[0, 0], [0, 0], [0, 0], [0, 0]])


Cargar.cargar_partida(tablero,posicionb1,posicionb2,posicionb3)
tablero = barco.barco1(tablero,posicionb1)
barco.barco2(tablero,posicionb2)
barco.barco3(tablero,posicionb3)
Juego.JuegoPro(posicionb1, posicionb2, posicionb3,tablerosinresolver,tablero)