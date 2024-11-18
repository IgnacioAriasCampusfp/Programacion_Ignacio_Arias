import sys
sys.path.append("Funciones")

from Funciones import Conexion_bbdd as cx
from Funciones import MenuMain as mn


cursor = cx.cursor
conexion = cx.conexion
mn.Menu(cursor,conexion)