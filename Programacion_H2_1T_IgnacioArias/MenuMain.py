from colorama import Fore as fr
from Funcionesmain import DAW_Main as dw

def Menu(cursor,conexion):
    
        while True:
            try:
                #Imprimir las opciones que tenemos, meternos en la funcion en expecifico.
                print(fr.BLUE+"=== Gestión de Tablas ===\nSeleccione una opción:\n1. Crear nuevo cliente\n2. Listar clientes y buscar\n3. Realizar compra\n4. Detalles pedido\n5. Salir"+fr.RESET)
                opcion = int(input("> "))
                match opcion:
                    case 1:
                        dw.Create(cursor,conexion)
                    case 2:
                        dw.List(cursor)
                    case 3:
                        dw.Buy(cursor,conexion)
                    case 4:
                        dw.Details(cursor,conexion)
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