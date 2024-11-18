from colorama import Fore as fr
from prettytable import PrettyTable


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
        # Crear una instancia de PrettyTable
        table = PrettyTable()
        
        # Listar todas las inscripciones relacionando tablas de la base de datos
        consulta = """
        SELECT 
            inscripciones.id_inscripcion, 
            clientes.nombre, 
            actividades.nombre_actividad, 
            actividades.horario  
        FROM 
            inscripciones 
        JOIN clientes ON inscripciones.id_cliente = clientes.id_cliente 
        JOIN actividades ON inscripciones.id_actividad = actividades.id_actividad;
        """
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        # Configurar los encabezados de la tabla
        table.field_names = ["ID Inscripción", "Cliente", "Actividad", "Horario"]

        # Agregar los resultados como filas
        for id_inscripcion, nombre, nombre_actividad, horario in resultados:
            table.add_row([id_inscripcion, nombre, nombre_actividad, horario])
        print(fr.CYAN + "Listado de Inscripciones:" + fr.RESET)
        print(table)
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