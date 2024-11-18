from colorama import Fore as fr


def Create(cursor, conexion):
    try:
        #Crear el entrenador ingresando los campos necesarios
        nombre_entrenador = input(fr.LIGHTCYAN_EX + "Ingrese el nombre del entrenador: " + fr.RESET)
        especialidad = input(fr.LIGHTCYAN_EX + "Ingrese la esepecialidad del entrenador: " + fr.RESET)
        
        #Hacer un insert para meter el entrenador
        consulta = """INSERT INTO entrenadores (nombre_entrenador, especialidad) VALUES ( %s, %s)"""
        cursor.execute(consulta, (nombre_entrenador,especialidad))
        conexion.commit()
        print(fr.GREEN + f"El entrenador '{nombre_entrenador}' ha sido creado con éxito." + fr.RESET)

    except ValueError as e:
        print(fr.RED + f"Error al crear un entrenador: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def List(cursor):
    try:
        #Listar todos los entrenadores
        consulta = "SELECT * FROM entrenadores;"
        cursor.execute(consulta)
        print(fr.CYAN + "Listado de Entrenadores:" + fr.RESET)
        resultados = cursor.fetchall()
        for identrenador, nombre, especialidad in resultados:
            print(fr.YELLOW + f"--->ID: {identrenador} Nombre: {nombre}, Especialidad: {especialidad}" + fr.RESET)            
        
    except ValueError as e:
        print(fr.RED + f"Error al listar entrenadores: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def Actu(cursor, conexion):
    
    try:
        #Actualizar entrenador en concreto pidiendo su informacion
        id_entrenador = input(fr.LIGHTCYAN_EX + "Ingrese el ID del entrenador: " + fr.RESET)
        nombre = input(fr.LIGHTCYAN_EX + "Ingrese el nombre actualizado del entrenador: " + fr.RESET).strip()
        especialidad = input(fr.LIGHTCYAN_EX + "Ingrese la especialidad actualizada del entrenador: " + fr.RESET)

        
        consulta = """
        UPDATE entrenadores SET nombre_entrenador=%s, especialidad=%s WHERE id_entrenador = %s
        """
        cursor.execute(consulta, (nombre,especialidad , id_entrenador))
        conexion.commit()
        print(fr.GREEN + f"El entrenador '{nombre}' ha sido actualizada con éxito." + fr.RESET)
        
        #Listar entrenadores ordenador por su id
        print(fr.CYAN + "Listado de Entrenadores Actualizado:" + fr.RESET)
        consulta = "SELECT * FROM entrenadores ORDER BY id_entrenador;"
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        for id_entrenador, nombre, especialidad ,  in resultados:
            print(fr.YELLOW + f"--->ID: {id_entrenador} Nombre: {nombre}, Especialidad: {especialidad}" + fr.RESET)            
  
    except ValueError as e:
        print(fr.RED + f"Error al actualizar un entrenador: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
            
        
def Delete(cursor, conexion):
    try:
        #Pedirle el id del entrenador que vamos a eliminar
        id_entrenador = input(fr.LIGHTCYAN_EX + "Ingrese el ID del entrenador que desea eliminar: " + fr.RESET)

        # Buscar actividades asociadas al entrenador
        consulta = "SELECT id_actividad FROM actividades WHERE id_entrenador = %s"
        cursor.execute(consulta, (id_entrenador,))
        resultados = cursor.fetchall()

        # Eliminar inscripciones relacionadas extrayendo el valor de id_actividad
        if resultados:
            for id_actividad in resultados:
                idactividad = id_actividad[0] 
                consulta = "DELETE FROM inscripciones WHERE id_actividad = %s"
                cursor.execute(consulta, (idactividad,))
                conexion.commit()

        # Eliminar actividades del entrenador
        consulta = "DELETE FROM actividades WHERE id_entrenador = %s"
        cursor.execute(consulta, (id_entrenador,))
        conexion.commit()

        # Eliminar el entrenador
        consulta = "DELETE FROM entrenadores WHERE id_entrenador = %s"
        cursor.execute(consulta, (id_entrenador,))
        conexion.commit()

        print(fr.GREEN + f"El entrenador con ID '{id_entrenador}' ha sido eliminado con éxito." + fr.RESET)

        
        
    except ValueError as e:
        print(fr.RED + f"Error al eliminar un entrenador: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)