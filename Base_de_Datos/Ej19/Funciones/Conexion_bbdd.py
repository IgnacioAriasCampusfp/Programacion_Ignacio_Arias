
from Funciones import funciones_bbdd as bdd


conexion = bdd.conectar("CENTRO_DEPORTIVO")
# Crear un cursor
cursor = conexion.cursor()