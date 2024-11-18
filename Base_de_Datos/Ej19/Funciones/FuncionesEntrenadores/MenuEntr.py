from Funciones.FuncionesEntrenadores import DAW_Entrenadores as dw

from colorama import Fore as fr

def Menu(cursor,conexion):
    
        while True:
            try:
                #Mostramos un menu con las distintas opciones del CRUD

                print(fr.BLUE+"=== Gestión de Entrenadores ===\nSeleccione una opción:\n1. Registrar entrenador\n2. Ver entrenadores\n3. Actualizar un entrenador\n4. Eliminar un entrenador\n5. Volver"+fr.RESET)
                opcion = int(input("> "))
                match opcion:
                    case 1:
                        dw.Create(cursor,conexion)
                    case 2:
                        dw.List(cursor)
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