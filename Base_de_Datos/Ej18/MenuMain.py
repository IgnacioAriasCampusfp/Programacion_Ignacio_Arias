import MenuCategoria as cm
import MenuProducto as pm
import MenuCliente as mc
import MenuPedido as mp
from colorama import Fore as fr

def Menu(cursor,conexion):
    
        while True:
            try:
                #Menu Global con todas las opciones
                print(fr.BLUE+"=== Gestión de Tablas ===\nSeleccione una opción:\n1. Tabla Categoria\n2. Tabla Producto\n3. Tabla Cliente\n4. Tabla Pedido \n5. Salir"+fr.RESET)
                opcion = int(input("> "))
                match opcion:
                    case 1:
                        cm.Menu(cursor,conexion)
                    case 2:
                        pm.Menu(cursor,conexion)
                    case 3:
                        mc.Menu(cursor,conexion)
                    case 4:
                        mp.Menu(cursor,conexion)
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