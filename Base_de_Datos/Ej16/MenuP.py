from Ej16.FuncionesProducto import DOW_producto as dw
import MenuM as mm
from colorama import Fore as fr

def Menu(cursor,conexion):
    
        while True:
            try:
                print(fr.BLUE+"=== Gestión de Productos ===\nSeleccione una opción:\n1. Crear nuevo producto\n2. Leer producto existente\n3. Actualizar un producto\n4. Eliminar un producto\n5. Salir"+fr.RESET)
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
                        print(fr.LIGHTRED_EX+"Volviendo al Menu Prinicpal"+fr.RESET)
                        
                        
                        break
                    case _:
                        print("Opción no valida")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
                
            except ValueError as e:
                print(f"No has ingresado una opción valida: {e}")