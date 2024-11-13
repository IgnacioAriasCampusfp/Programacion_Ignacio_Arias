from colorama import Fore as fr

def Create(cursor, conexion):
    try:
        idcategoria = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID de la nueva categoría: " + fr.RESET))
        categoria = input(fr.LIGHTCYAN_EX + "Ingrese el nombre de la nueva categoría: " + fr.RESET).strip()
        
        consulta = """INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)"""
        cursor.execute(consulta, (idcategoria, categoria))
        conexion.commit()
        print(fr.GREEN + f"La categoría '{categoria}' ha sido creada con éxito." + fr.RESET)
        
        print(fr.CYAN + "Listado de Categorías:" + fr.RESET)
        consulta = "SELECT * FROM categoria ORDER BY idcategoria;"
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        for idcategoria, categoria in resultados:
            print(fr.YELLOW + f"ID: {idcategoria}, Categoria: {categoria}" + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al crear una nueva categoría: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def List(cursor, conexion):
    try:
        consulta = "SELECT * FROM categoria;"
        cursor.execute(consulta)
        
        print(fr.CYAN + "Listado de Categorías:" + fr.RESET)
        resultados = cursor.fetchall()
        for idcategoria, categoria in resultados:
            print(fr.YELLOW + f"ID: {idcategoria}, Categoria: {categoria}" + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al listar categorías: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def Actu(cursor, conexion):
    try:
        idcategoria = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID de la categoría que desea actualizar: " + fr.RESET))
        categoria = input(fr.LIGHTCYAN_EX + "Ingrese el nuevo nombre de la categoría: " + fr.RESET)
        
        consulta = "UPDATE categoria SET categoria = %s WHERE idcategoria = %s"
        cursor.execute(consulta, (categoria, idcategoria))
        conexion.commit()
        print(fr.GREEN + f"La categoría '{categoria}' ha sido actualizada con éxito." + fr.RESET)
        
        print(fr.CYAN + "Listado de Categorías Actualizado:" + fr.RESET)
        consulta = "SELECT * FROM categoria ORDER BY idcategoria;"
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        for idcategoria, categoria in resultados:
            print(fr.YELLOW + f"ID: {idcategoria}, Categoria: {categoria}" + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al actualizar una categoría: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def Delete(cursor, conexion):
    try:
        idcategoria = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID de la categoría que desea eliminar: " + fr.RESET))
        
        consulta = "DELETE FROM categoria WHERE idcategoria = %s"
        cursor.execute(consulta, (idcategoria,))
        conexion.commit()
        print(fr.GREEN + f"La categoría con ID '{idcategoria}' ha sido eliminada con éxito." + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al eliminar una categoría: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
