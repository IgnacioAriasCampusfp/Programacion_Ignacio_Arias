from Funciones import DOW_categoria as dw
from colorama import Fore as fr

def Menu(cursor,conexion):
    try:
        while True:
            print(fr.BLUE+"=== Gestión de Categorías ===\nSeleccione una opción:\n1. Crear nueva categoría\n2. Leer categorías existentes\n3. Actualizar una categoría\n4. Eliminar una categoría\n5. Salir"+fr.RESET)
            opcion = int(input("> "))
            match opcion:
                case 1:
                    dw.Create(cursor,conexion)
                case 2:
                    dw.List(cursor,conexion)
                case 3:
                    dw.Actu(cursor,conexion)
                case 4:
                    dw.Delete(cursor,conexion)
                case 5:
                    print(fr.LIGHTRED_EX+"Cerrando base de datos y saliendo del programa"+fr.RESET)
                    cursor.close()
                    conexion.close()
                    break
                case _:
                    print("Opción no valida")
    except Exception as e:
        print(fr.RED+f"Ocurrió un error inesperado: {e} " + fr.RESET)
        Menu(cursor,conexion)
    except ValueError as e:
        print(fr.RED+f"No has ingresado una opción valida: {e}"+ fr.RESET)
        Menu(cursor,conexion)