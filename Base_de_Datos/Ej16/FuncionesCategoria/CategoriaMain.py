import sys
sys.path.append("Funciones")

import Conexion_bbdd as cx
import Ej16.MenuC as mn


cursor = cx.cursor
conexion = cx.conexion
mn.Menu(cursor,conexion)