from colorama import Fore as fr
import numpy as np
import datetime as dt

def Create(cursor, conexion):
    try:
        idcliente = input("Que id cliente eres/es: ").upper()
        idpedido = int(input("¿Qué número de pedido es este?: "))
        FechaP =  dt.datetime.now()
        FechaE = FechaP + np.timedelta64(2, 'D')
        consulta = """INSERT INTO pedido (idpedido, idcliente, fechapedido, fechaentrega) VALUES (%s, %s,%s, %s)"""
        cursor.execute(consulta, (idpedido,idcliente,FechaP,FechaE ))
        conexion.commit()
        print(fr.CYAN + "Listado de Productos:" + fr.RESET)
        consulta = "SELECT * FROM producto ORDER BY idproducto;"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        for idproducto, nombre, idcategoria, medida, precio, stock in resultados:
            print(f"{fr.YELLOW}IDproducto: {idproducto}, Nombre: {nombre}, IdCategoria: {idcategoria}, Medida: {medida}, Precio: {precio}, Stock: {stock}{fr.RESET}")

        while True:
             #Seleccionar el producto y las cantidades
            idproducto = input("Que producto quieres añadir al carrito: ")
            unidades = int(input("Cuanta cantidad de este producto: "))
            descuento = float(input("¿Este producto tiene algun descuento?: "))
            #Imprimir el producto seleccionado
            
            consulta = "SELECT * FROM producto WHERE idproducto= %s;"
            cursor.execute(consulta,(idproducto,))
            resultados = cursor.fetchall()
            for idproducto, nombre, idcategoria, medida, precio, stock in resultados:
                print(f"{fr.YELLOW}IDproducto: {idproducto}, Nombre: {nombre}, IdCategoria: {idcategoria}, Medida: {medida}, Precio: {precio}, Stock: {stock}{fr.RESET}")
                precioproducto = precio
            #Insertar en la tabla detalle los productos seleccionados anteriormente
            consulta = """INSERT INTO detalle (idpedido, idproducto, precio, unidades, descuento) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(consulta, (idpedido, idproducto, precioproducto, unidades, descuento))
            conexion.commit()
                
            #Una opcion para continuar o no
            opcion = input("¿Desea Continuar? Si/No ").lower()
            if opcion == "no":
                break
            else:
                continue
            
                   
    except ValueError as e:
        print(fr.RED + f"Error al crear un nuevo pedido: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def List(cursor, conexion):
    try:
        consulta = "SELECT pedido.*, detalle.idproducto, detalle.precio, detalle.unidades, detalle.descuento FROM detalle inner join pedido on detalle.idpedido = pedido.idpedido order by detalle.idpedido;"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        print(fr.CYAN + "Listado de Detalle:" + fr.RESET)
        for idpedido, idcliente, FechaP, FechaE , idproducto, precio, unidades, descuento in resultados:
            print(fr.YELLOW+f"IDpedido: {idpedido}, IDCliente:{idcliente}, FechaPedido:{FechaP}, FechaEntrega:{FechaE}  IDproducto: {idproducto}, Precio: {precio}, Unidades: {unidades}, Descuento: {descuento}"+ fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al listar pedidos: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def Actu(cursor, conexion):
    try:
       
        consulta = "SELECT pedido.*, detalle.idproducto, detalle.precio, detalle.unidades, detalle.descuento FROM detalle inner join pedido on detalle.idpedido = pedido.idpedido order by detalle.idpedido DESC LIMIT 10;"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        print(fr.CYAN + "Listado de Detalle:" + fr.RESET)
        for idpedido, idcliente, FechaP, FechaE , idproducto, precio, unidades, descuento in resultados:
            print(fr.YELLOW+f"IDpedido: {idpedido}, IDCliente:{idcliente}, FechaPedido:{FechaP}, FechaEntrega:{FechaE}  IDproducto: {idproducto}, Precio: {precio}, Unidades: {unidades}, Descuento: {descuento}"+ fr.RESET)
        idpedido = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID del pedido que quieras modificar: " + fr.RESET))
        while True:
            opcion= int(input("Que quieres modificar:\n 1. IDcliente \n2. IDProducto \n3. Unidades \n4. Descuento\n5. Nada mas\n>"))
            match opcion:
                case 1:
                    idcliente = input("Que id cliente es el correcto: ").upper()
                    consulta = """
                    UPDATE pedido SET idcliente = %s WHERE idpedido = %s
                    """
                    cursor.execute(consulta, (idcliente, idpedido, ))
                    conexion.commit()
                    print(fr.GREEN + f"El pedido '{idpedido}' ha sido actualizado con éxito." + fr.RESET)
                    continue
                case 2:
                    productoerror = int(input("Que idproducto es cual esta mal: "))
                    idproducto = int(input("Que producto es el correcto: "))

                    # Obteniendo el precio correcto del producto
                    consulta = "SELECT precio FROM producto WHERE idproducto = %s;"
                    cursor.execute(consulta, (idproducto,))
                    resultados = cursor.fetchall()

                    # Extrae el valor del precio de la tupla obtenida
                    for precio in resultados:
                        precioproducto = precio[0]  # Accede al primer elemento de la tupla

                    consulta = """
                        UPDATE detalle SET idproducto = %s, precio = %s WHERE idpedido = %s AND idproducto = %s
                    """
                    cursor.execute(consulta, (idproducto, precioproducto, idpedido, productoerror))
                    conexion.commit()
                    print(fr.GREEN + f"El pedido '{idpedido}' ha sido actualizado con éxito." + fr.RESET)
                    continue
                case 3:
                    productoerror = int(input("Que idproducto es cual esta mal: "))
                    unidades = int(input("Cuantas unidades son en realidad: "))

                    consulta = """
                        UPDATE detalle SET unidades = %s WHERE idpedido = %s AND idproducto = %s
                    """
                    cursor.execute(consulta, (unidades, idpedido, productoerror))
                    conexion.commit()

                    print(fr.GREEN + f"El pedido '{idpedido}' ha sido actualizado con éxito." + fr.RESET)
                    continue
                case 4:
                    productoerror = int(input("Que idproducto es cual esta mal: "))                    
                    descuento = float(input("Cual es el descuento real?: "))
                    consulta = """
                    UPDATE detalle SET descuento = %s WHERE idpedido = %s AND idproducto = %s
                    """
                    cursor.execute(consulta, (descuento, idpedido, productoerror))
                    conexion.commit()
                    print(fr.GREEN + f"El pedido '{idpedido}' ha sido actualizado con éxito." + fr.RESET)
                    continue
                case 5:
                    break
                    
            
            

    except ValueError as e:
        print(fr.RED + f"Error al actualizar un producto: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def Delete(cursor, conexion):
    try:
        idpedido = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID del pedido que quieres eliminar: " + fr.RESET))
        
        consulta = "DELETE FROM detalle WHERE idpedido = %s"
        cursor.execute(consulta, (idpedido,))
        conexion.commit()
        consulta = "DELETE FROM pedido WHERE idpedido = %s"
        cursor.execute(consulta, (idpedido,))
        conexion.commit()
        print(fr.GREEN + f"El producto con ID '{idpedido}' ha sido eliminado con éxito." + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al eliminar un producto: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
