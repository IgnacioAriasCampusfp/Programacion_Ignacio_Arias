from colorama import Fore as fr
#Importar Menus de cada Función
from Funciones.FuncionesCliente import MenuClie as mc 
from Funciones.FuncionesActividades import MenuAct as ma
from Funciones.FuncionesEntrenadores import MenuEntr as me
from Funciones.FuncionesInscripciones import MenuInsc as mi


def Menu(cursor,conexion):
    
        while True:
            try:
                #Menu Global con todas las opciones
                print(fr.BLUE+"=== Gestión de Tablas ===\nSeleccione una opción:\n1. Gestión de Clientes\n2. Gestión de Actividades\n3. Gestión de Entrenadores\n4. Gestión de Inscripciones \n5. Salir"+fr.RESET)
                opcion = int(input("> "))
                match opcion:
                    case 1:
                        mc.Menu(cursor,conexion)
                    case 2:
                        ma.Menu(cursor,conexion)
                    case 3:
                        me.Menu(cursor,conexion)
                    case 4:
                        mi.Menu(cursor,conexion)
                    case 5:
                        print(fr.LIGHTRED_EX+"Cerrando base de datos y saliendo del programa"+fr.RESET)
                        cursor.close()
                        conexion.close()
                        break
                    case _:
                        print("Opción no valida")
            except Exception as e:
                print(fr.RED+f"Ocurrió un error inesperado: {e} " + fr.RESET)
                
            except ValueError as e:
                print(fr.RED+f"No has ingresado una opción valida: {e}"+ fr.RESET)