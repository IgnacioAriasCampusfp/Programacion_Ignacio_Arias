from FuncionesCategoria import DOW_categoria as dw
from colorama import Fore as fr
import MenuM as mm

def Menu(cursor,conexion):
    
        while True:
            try:
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
                        print(fr.LIGHTRED_EX+"Volviendo al Menu Prinicpal"+fr.RESET)
                        
                        break
                    case _:
                        print("Opción no valida")
            except Exception as e:
                print(fr.RED+f"Ocurrió un error inesperado: {e} " + fr.RESET)
                
            except ValueError as e:
                print(fr.RED+f"No has ingresado una opción valida: {e}"+ fr.RESET)
                