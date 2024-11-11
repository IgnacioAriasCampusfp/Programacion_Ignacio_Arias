
from Funcionesmain import funciones_bbdd as bdd


conexion = bdd.conectar("SUPERMERCADOPython")
# Crear un cursor
cursor = conexion.cursor()