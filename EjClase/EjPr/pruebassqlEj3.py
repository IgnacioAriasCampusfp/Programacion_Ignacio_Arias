import funciones_bbdd as bdd

conexion = bdd.conectar("Animales")

# Crear un cursor
cursor = conexion.cursor()

nuevo_animal = (10,2,"Tigre",2)

# Escribir la consulta SQL
consulta = """
INSERT INTO ANIMAL (idAnimal, idFamilia, animal, cuantos) VALUES (%s, %s, %s, %s)
"""



# Ejecutar la consulta
cursor.execute(consulta,nuevo_animal)
conexion.commit()
print("Nuevo animal insertado correctamente")

consulta = """
SELECT ANIMAL.animal, FAMILIA.familia
FROM ANIMAL
JOIN FAMILIA ON ANIMAL.idFamilia = FAMILIA.idfamilia
ORDER BY idanimal;
"""
cursor.execute(consulta)
# Obtener y mostrar los resultados
resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta
for familia, total in resultados:
    print(f"Familia: {familia}, Total de animales: {total}")



# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
