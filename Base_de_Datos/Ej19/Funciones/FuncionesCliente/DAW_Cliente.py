from colorama import Fore as fr
from pathlib import Path
import numpy as np 


def Create(cursor, conexion):
    try:
        opcion = int(input("eleccion"))
        match opcion:
            case 1:
                #Crear cliente pidiendole nombre, edad y el tipo de membresia
                nombre = input(fr.LIGHTCYAN_EX + "Ingrese el nombre del cliente: " + fr.RESET)
                edad = int(input(fr.LIGHTCYAN_EX + "Ingrese la edad del cliente: " + fr.RESET))  
                tipo_membresia = input(fr.LIGHTCYAN_EX +"Ingrese la membresia cliente: "+ fr.RESET)
                #Hacer un insert para meter el cliente
                consulta = """INSERT INTO clientes (nombre, edad,tipo_membresia) VALUES (%s, %s, %s)"""
                "Create table cliente (nombre varchar(50), Telefono int, )"
                cursor.execute(consulta, (nombre,edad,tipo_membresia))
                conexion.commit()
                print(fr.GREEN + f"El cliente '{nombre}' ha sido creado con éxito." + fr.RESET)
            case 2:


                archivo = Path("ClientesImp.txt")

                if archivo.exists():
                    try:
                        with open(archivo, "r") as archivo:
                            lineas = archivo.readlines()[:3]

                            if len(lineas) < 3:
                                raise ValueError("El archivo no contiene suficientes líneas para procesar los datos.")

                            # Convertir las líneas en un array y asignar las variables
                            array1 = np.array([linea.strip() for linea in lineas])
                            nombre = str(array1[0])  # Convertir a cadena estándar de Python
                            edad = int(array1[1])    # Convertir a entero estándar de Python
                            membresia = str(array1[2])


                            

                            # Insertar en la base de datos
                            consulta = """INSERT INTO clientes (nombre, edad, tipo_membresia) VALUES (%s, %s, %s)"""
                            cursor.execute(consulta, (nombre, edad, membresia))
                            conexion.commit()
                            print("Datos insertados correctamente.")
                    except Exception as e:
                        print(f"Se produjo un error: {e}")
                else:
                    print("El archivo no existe.")




    except ValueError as e:
        print(fr.RED + f"Error al crear un cliente: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def List(cursor):
    try:
        #Listar todos los clientes
        consulta = "SELECT * FROM clientes;"
        cursor.execute(consulta)
        print(fr.CYAN + "Listado de Clientes:" + fr.RESET)
        resultados = cursor.fetchall()
        for idcliente, nombre, edad, tipo_membresia in resultados:
            print(fr.YELLOW + f"--->ID: {idcliente} Nombre: {nombre}, Edad: {edad} Tipo de Membresia: {tipo_membresia} " + fr.RESET)            
        
    except ValueError as e:
        print(fr.RED + f"Error al listar clientes: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def Actu(cursor, conexion):
    
    try:
        #Actualizar cliente pidiendole su id, nombre, edad y el tipo de membresia
        
        id_cliente = input(fr.LIGHTCYAN_EX + "Ingrese el ID del cliente: " + fr.RESET)
        nombre = input(fr.LIGHTCYAN_EX + "Ingrese el nuevo nombre del cliente: " + fr.RESET).strip()
        edad = input(fr.LIGHTCYAN_EX + "Ingrese la nueva edad del cliente: " + fr.RESET)
        tipo_membresia = input(fr.LIGHTCYAN_EX + "Ingrese la nueva membresia del cliente: " + fr.RESET)

        #Consulta para actualizar el cliente
        consulta = """
        UPDATE clientes SET nombre=%s, edad=%s, tipo_membresia=%s WHERE id_cliente = %s
        """
        cursor.execute(consulta, (nombre, edad, tipo_membresia, id_cliente))
        conexion.commit()
        print(fr.GREEN + f"El cliente '{nombre}' ha sido actualizada con éxito." + fr.RESET)
        
        print(fr.CYAN + "Listado de Clientes Actualizado:" + fr.RESET)
        consulta = "SELECT * FROM clientes ORDER BY id_cliente;"
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        for idcliente, nombre, edad, tipo_membresia in resultados:
            print(fr.YELLOW + f"--->ID: {idcliente} Nombre: {nombre}, Edad: {edad} Tipo de Membresia: {tipo_membresia} " + fr.RESET)            
  
    except ValueError as e:
        print(fr.RED + f"Error al actualizar un cliente: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
            
        
def Delete(cursor, conexion):
    try:
        #Le pedimos que nos de el id del cliente que queramos eliminar
        idcliente = input(fr.LIGHTCYAN_EX + "Ingrese el ID del cliente que desea eliminar: " + fr.RESET)
        #Primero eliminamos si estamos en alguna inscripcion por que osino nos da error
        consulta = "Delete from inscripciones where id_cliente = %s"
        cursor.execute(consulta, (idcliente,))
        conexion.commit()
        #Seguido eliminamos el cliente de la tabla clientes
        consulta = "DELETE FROM clientes WHERE id_cliente = %s"
        cursor.execute(consulta, (idcliente,))
        conexion.commit()
        
        print(fr.GREEN + f"El cliente con ID '{idcliente}' ha sido eliminado con éxito." + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al eliminar un cliente: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
