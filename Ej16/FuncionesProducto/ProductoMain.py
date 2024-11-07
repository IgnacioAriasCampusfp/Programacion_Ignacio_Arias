import sys
sys.path.append("Ej16/Funciones")

import Conexion_bbdd as cx
import Ej16.MenuP as mn


cursor = cx.cursor
conexion = cx.conexion
mn.Menu(cursor,conexion)