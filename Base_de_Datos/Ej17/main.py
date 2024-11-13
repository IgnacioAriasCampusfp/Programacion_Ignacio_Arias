import sys
sys.path.append("Funciones")

from Funcionesmain import Conexion_bbdd as cx
import MenuMain as mn


cursor = cx.cursor
conexion = cx.conexion
mn.Menu(cursor,conexion)