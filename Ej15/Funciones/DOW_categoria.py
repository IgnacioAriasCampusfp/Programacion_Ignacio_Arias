from colorama import Fore as fr
def Create(cursor,conexion):
    try:
        idcategoria = int(input("Ingrese el ID de la nueva categoría: "))
        categoria = input("Ingrese el nombre de la nueva categoría: ").strip()
        consulta = """INSERT INTO categoria (idcategoria , categoria) VALUES (%s, %s)"""
        cursor.execute(consulta,(idcategoria,categoria))
        conexion.commit()
        print(fr.GREEN+f"La categoría '{categoria}' ha sido creada con éxito."+fr.RESET)
        
        print(fr.GREEN+"Listado de Categorías:"+fr.RESET)
        consulta = """
        SELECT*FROM categoria
        ORDER BY idcategoria;
        """
        cursor.execute(consulta)
        # Obtener y mostrar los resultados
        resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        for idcategoria,categoria in resultados:
            print(fr.CYAN+f"ID: {idcategoria}, Categoria: {categoria}"+fr.RESET)
        
    except ValueError as e:
        print(fr.RED+f"Error al crear una nueva categoria: {e}"+fr.RESET)
    except Exception as e:
        print(fr.RED+f"Ocurrió un error inesperado: {e}"+fr.RESET)
        
def List(cursor,conexion):
    try:
        consulta = """
        SELECT *
        FROM categoria;
        """
        cursor.execute(consulta)
        # Obtener y mostrar los resultados
        resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        for idcategoria,categoria in resultados:
            print(fr.CYAN+f"ID: {idcategoria}, Categoria: {categoria}"+fr.RESET)
        
    except ValueError as e:
        print(fr.RED+f"Error al crear una actualizar categoria: {e}"+fr.RESET)
    except Exception as e:
        print(fr.RED+f"Ocurrió un error inesperado: {e}"+fr.RESET)


def Actu(cursor,conexion):
    try:
        idcategoria = int(input("Ingrese el IDcategoria que quieras actualizar: "))
        categoria = input("Ingrese el nombre de la categoría actualizada: ")
        consulta = """UPDATE categoria SET categoria = %s WHERE idcategoria = %s"""
        cursor.execute(consulta,(categoria, idcategoria))
        conexion.commit()
        print(fr.GREEN+f"La categoría '{categoria}' ha sido actualizada con éxito."+fr.RESET)
        
        print("Listado de Categorías Actualizada:")
        consulta = """
        SELECT*FROM categoria
        ORDER BY idcategoria;
        """
        cursor.execute(consulta)
        # Obtener y mostrar los resultados
        resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        for idcategoria,categoria in resultados:
            print(fr.CYAN+f"ID: {idcategoria}, Categoria: {categoria}"+fr.RESET)
        
    except ValueError as e:
        print(fr.RED+f"Error al crear una actualizar categoria: {e}"+fr.RESET)
    except Exception as e:
        print(fr.RED+f"Ocurrió un error inesperado: {e}"+fr.RESET)



def Delete(cursor,conexion):
    try:
        idcategoria = int(input("Ingrese el ID de la categoría que quieras eliminar: "))
        
        consulta = "DELETE FROM categoria WHERE idcategoria = %s"
        cursor.execute(consulta, (idcategoria,))
        conexion.commit()
        print(fr.GREEN+f"El idcategoria '{idcategoria}' ha sido eliminada con éxito."+fr.RESET)
        
        
    except ValueError as e:
        print(fr.RED+f"Error al crear una nueva categoria: {e}"+fr.RESET)
    except Exception as e:
        print(fr.RED+f"Ocurrió un error inesperado: {e}"+fr.RESET)