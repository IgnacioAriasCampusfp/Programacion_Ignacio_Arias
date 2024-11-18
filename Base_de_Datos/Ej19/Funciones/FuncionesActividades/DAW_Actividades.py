from colorama import Fore as fr


def Create(cursor, conexion):
    try:
        #Crear la actividad asociando el entrenador con el
        nombre_actividad = input(fr.LIGHTCYAN_EX + "Ingrese el nombre de la actividad: " + fr.RESET)
        horario = input(fr.LIGHTCYAN_EX + "Ingrese el horario: " + fr.RESET)
        duracion = int(input(fr.LIGHTCYAN_EX +"Ingrese la duracion de la actividad (minutos): "+ fr.RESET))
        id_entrenador = input(fr.LIGHTCYAN_EX +"Ingrese el entrenador a cargo: "+ fr.RESET)
        #Hacer un insert para meter el cliente
        consulta = """INSERT INTO actividades (nombre_actividad,horario,duracion, id_entrenador) VALUES (%s, %s, %s,%s)"""
        cursor.execute(consulta, (nombre_actividad,horario,duracion, id_entrenador))
        conexion.commit()
        print(fr.GREEN + f"La actividad '{nombre_actividad}' ha sido creado con éxito." + fr.RESET)

    except ValueError as e:
        print(fr.RED + f"Error al crear una actividad: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def List(cursor):
    try:
        #Listar todas las actividades referenciando tambien el nombre del entrenador
        consulta = "SELECT actividades.*, entrenadores.nombre_entrenador FROM actividades join entrenadores on actividades.id_entrenador = entrenadores.id_entrenador;"
        cursor.execute(consulta)
        print(fr.CYAN + "Listado de Actividades:" + fr.RESET)
        resultados = cursor.fetchall()
        for id_actividad, nombre_actividad,horario,duracion, identrenador, nombre in resultados:
            print(fr.YELLOW + f"--->ID: {id_actividad} Actividad: {nombre_actividad}, Horario: {horario}, Duración: {duracion}, Entrenador:{identrenador}, Nombre:{nombre}  " + fr.RESET)            
        
    except ValueError as e:
        print(fr.RED + f"Error al listar actividades: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def Actu(cursor, conexion):
    
    try:
        #Actualizar la actividad pidiendole la informacion necesaria
        id_actividad = input(fr.LIGHTCYAN_EX + "Ingrese el ID de la actividad: " + fr.RESET)
        nombre_actividad = input(fr.LIGHTCYAN_EX + "Ingrese el nombre de la actividad actualizado: " + fr.RESET)
        horario = input(fr.LIGHTCYAN_EX + "Ingrese el horario actualizado: " + fr.RESET)
        duracion = int(input(fr.LIGHTCYAN_EX +"Ingrese la duracion de la actividad (minutos) actualizado: "+ fr.RESET))
        id_entrenador = input(fr.LIGHTCYAN_EX +"Ingrese el entrenador a cargo actualizado: "+ fr.RESET)
        
        consulta = """
        UPDATE clientes SET nombre_actividad=%s, horario=%s, duracion=%s,id_entrenador =%s  WHERE id_actividad = %s
        """
        cursor.execute(consulta, (nombre_actividad, horario, duracion, id_entrenador,id_actividad))
        conexion.commit()
        print(fr.GREEN + f"El cliente '{nombre_actividad}' ha sido actualizada con éxito." + fr.RESET)
        
        #Mostrar una lista actualizada con los nuevos datos
        print(fr.CYAN + "Listado de Actividades Actualizado:" + fr.RESET)
        consulta = "SELECT actividades.*, entrenadores.nombre_entrenador FROM actividades join entrenadores on actividades.id_entrenador = entrenadores.id_entrenador;"
        cursor.execute(consulta)
        print(fr.CYAN + "Listado de Actividades:" + fr.RESET)
        resultados = cursor.fetchall()
        for id_actividad, nombre_actividad,horario,duracion, identrenador, nombre in resultados:
            print(fr.YELLOW + f"--->ID: {id_actividad} Actividad: {nombre_actividad}, Horario: {horario}, Duración: {duracion}, Entrenador:{identrenador}, Nombre:{nombre}  " + fr.RESET)            

    except ValueError as e:
        print(fr.RED + f"Error al actualizar una actividad: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
            
        
def Delete(cursor, conexion):
    try:
        #Pedirle el id que quiere eliminar y usandolo primero en inscripciones y luego en actividades para que no de error
        id_actividad = input(fr.LIGHTCYAN_EX + "Ingrese el ID de la actividad que desea eliminar: " + fr.RESET)
        consulta = "Delete from inscripciones where id_actividad = %s"
        cursor.execute(consulta, (id_actividad,))
        conexion.commit()
        
        consulta = "DELETE FROM actividades WHERE id_actividad = %s"
        cursor.execute(consulta, (id_actividad,))
        conexion.commit()
        
        print(fr.GREEN + f"El cliente con ID '{id_actividad}' ha sido eliminado con éxito." + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al eliminar una actividad: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)