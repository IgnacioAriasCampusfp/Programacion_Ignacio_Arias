from colorama import Fore as fr


def Create(cursor, conexion):
    try:
        #Crear inscripciones pidiendole el cliente y la actividad
        id_cliente = int(input(fr.LIGHTCYAN_EX + "Ingrese el idcliente para la incripcion: " + fr.RESET))
        id_actividad = int(input(fr.LIGHTCYAN_EX + "Ingrese el id de la actividad a la que se va a registrar: " + fr.RESET))

        #Hacer un insert para meter la inscripcion en la base de datos
        consulta = """INSERT INTO inscripciones (id_cliente,id_actividad) VALUES (%s, %s)"""
        cursor.execute(consulta, (id_cliente,id_actividad))
        conexion.commit()
        print(fr.GREEN + f"La incripcion ha sido creado con éxito." + fr.RESET)

    except ValueError as e:
        print(fr.RED + f"Error al crear una inscripción: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def List(cursor):
    try:
        #Listar todas las inscripciones relacionando tablas de la base de datos
        consulta = "SELECT inscripciones.id_inscripcion, clientes.nombre, actividades.nombre_actividad, actividades.horario  FROM inscripciones join clientes on inscripciones.id_cliente = clientes.id_cliente join actividades on inscripciones.id_actividad = actividades.id_actividad;"
        cursor.execute(consulta)
        print(fr.CYAN + "Listado de Actividades:" + fr.RESET)
        resultados = cursor.fetchall()
        for id_inscripcion, nombre, nombre_actividad, horario in resultados:
            print(fr.YELLOW + f"\nID Inscripción    | Cliente        | Actividad       | Horario\n------------------------------------------------------------------\n {id_inscripcion}                | {nombre}          | {nombre_actividad}            | {horario}            " + fr.RESET)                      
        
    except ValueError as e:
        print(fr.RED + f"Error al listar inscripciones: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
     
def Delete(cursor, conexion):
    try:
        #Pedir el id de inscripcion para su eliminacion
        id_inscripcion = int(input(fr.LIGHTCYAN_EX + "Ingrese el id de inscripcion para eliminarlo: " + fr.RESET))


        consulta = "Delete from inscripciones where id_inscripcion = %s"
        cursor.execute(consulta, (id_inscripcion,))
        conexion.commit()
        

        
        print(fr.GREEN + f"La inscripcion con ID '{id_inscripcion}' ha sido eliminado con éxito." + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al eliminar una inscripcion: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)