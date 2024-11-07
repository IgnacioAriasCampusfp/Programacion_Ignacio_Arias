
from Funciones import funciones_bbdd as bdd


conexion = bdd.conectar("Supermercado")
# Crear un cursor
cursor = conexion.cursor()