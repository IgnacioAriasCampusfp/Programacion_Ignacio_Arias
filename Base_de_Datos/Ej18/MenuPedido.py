from FuncionesPedido_Det import DAW_pedido as dw

from colorama import Fore as fr

def Menu(cursor,conexion):
    
        while True:
            try:
                print(fr.BLUE+"=== Gestión de Pedidos ===\nSeleccione una opción:\n1. Realizar pedido\n2. Leer pedido existente\n3. Actualizar un pedido\n4. Eliminar un pedido\n5. Salir"+fr.RESET)
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