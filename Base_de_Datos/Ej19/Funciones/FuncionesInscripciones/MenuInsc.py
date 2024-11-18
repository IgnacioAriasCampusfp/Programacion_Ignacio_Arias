from Funciones.FuncionesInscripciones import DAW_Inscripciones as dw

from colorama import Fore as fr

def Menu(cursor,conexion):
    
        while True:
            try:
                #Mostramos un menu con las distintas opciones del CRUD

                print(fr.BLUE+"=== Gestión de Clientes ===\nSeleccione una opción:\n1. Registrar inscripción \n2. Ver inscripción\n3. Eliminar inscripción\n4. Volver"+fr.RESET)
                opcion = int(input("> "))
                match opcion:
                    case 1:
                        dw.Create(cursor,conexion)
                    case 2:
                        dw.List(cursor)
                    case 3:
                        dw.Delete(cursor,conexion)
                    case 4:
                        print(fr.LIGHTRED_EX+"Volviendo al Menu Prinicpal"+fr.RESET)
                        
                        
                        break
                    case _:
                        print("Opción no valida")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
                
            except ValueError as e:
                print(f"No has ingresado una opción valida: {e}")