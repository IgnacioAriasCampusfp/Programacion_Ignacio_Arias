from colorama import Fore as fr
import numpy as np
from pathlib import Path

def Create(cursor, conexion):
    try:
        #Crear cliente
        nombre = input(fr.LIGHTCYAN_EX + "Ingrese el nombre del cliente: " + fr.RESET)
        ciudad = input(fr.LIGHTCYAN_EX + "Ingrese la ciudad del cliente: " + fr.RESET)
        tlf = int(input(fr.LIGHTCYAN_EX +"Ingrese el telefono del cliente: "+ fr.RESET))
        #Hacer un insert para meter el cliente
        consulta = """INSERT INTO cliente (Nombre, ciudad,tlf) VALUES (%s, %s, %s)"""
        cursor.execute(consulta, (nombre,ciudad,tlf))
        conexion.commit()
        print(fr.GREEN + f"El cliente '{nombre}' ha sido creado con éxito." + fr.RESET)

    except ValueError as e:
        print(fr.RED + f"Error al crear un cliente: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def List(cursor):
    try:
        #Listar todos los clientes
        consulta = "SELECT * FROM cliente;"
        cursor.execute(consulta)
        #Comprobar si el archivo de texto existe
        archivo = Path("List_Cliente.txt")
        
        if archivo.exists():
            archivo.unlink()
        
        print(fr.CYAN + "Listado de Clientes:" + fr.RESET)
        resultados = cursor.fetchall()
        for idcliente, nombre,ciudad,tlf in resultados:
            print(fr.YELLOW + f"--->ID: {idcliente} Nombre: {nombre}, Ciudad: {ciudad} Tlf: {tlf} " + fr.RESET)
        array = np.array(resultados)

        # Guardar en archivo
        with open("List_Cliente.txt", "w") as archivo:
            for fila in array:
                archivo.write(", ".join(map(str, fila)) + "\n")
        
        #Le pedimos que cliente quiere buscar
        idcliente = input("Que cliente quieres buscar dime su ID: ")
        
        #Buscas al cliente donde el cliente es el que has seleccionado
        consulta = "SELECT * FROM cliente WHERE idcliente = %s;"
        cursor.execute(consulta, (idcliente,))
        
        resultados = cursor.fetchall()
        #Imprimir el cliente seleccionado
        for idcliente, nombre,ciudad,tlf in resultados:
            print(fr.YELLOW + f"--->ID: {idcliente} Nombre: {nombre}, Ciudad: {ciudad} Tlf: {tlf} " + fr.RESET)
        
            
        
    except ValueError as e:
        print(fr.RED + f"Error al listar clientes: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def Buy(cursor, conexion):
    
    try:
        #Identidicar al cliente
        idcliente=input("Identificate, ¿Que cliente eres?: ")
        #ID pedido
        idpedido=int(input("¿Que pedido es este?: "))
        
        #Mostrar todos los productos
        consulta = "SELECT * FROM producto;"
        cursor.execute(consulta)
        #Listar productos
        print(fr.CYAN + "Listado de Productos:" + fr.RESET)
        resultados = cursor.fetchall()
        for idproducto, nombre,precio in resultados:
            print(fr.YELLOW + f"--->ID: {idproducto} Nombre: {nombre}, Precio: {precio} " + fr.RESET)
        
        #Insertar en la tabla pedido el idcliente para registrarlo
        consulta = """INSERT INTO pedido (idpedido,idcliente) VALUES (%s,%s)"""
        cursor.execute(consulta, (idpedido,idcliente))
        conexion.commit()
            
        while True:
            #Seleccionar el producto y las cantidades
            idproducto = input("Que producto quieres añadir al carrito: ")
            unidades = input("Cuanta cantidad de este producto: ")
            #Imprimir el producto seleccionado
            consulta = "SELECT * FROM producto WHERE idproducto = %s;"
            cursor.execute(consulta, (idproducto,))
            resultados = cursor.fetchall()
            for idproducto, nombre,precio in resultados:
                print(fr.YELLOW + f"--->Producto Seleccionado: ID: {idproducto} Nombre: {nombre}, Precio: {precio} " + fr.RESET)
                precioproducto = precio

            
            #Insertar en la tabla detalle los productos seleccionados anteriormente
            consulta = """INSERT INTO detalle (idpedido, idproducto, precio, unidades) VALUES (%s, %s, %s, %s)"""
            cursor.execute(consulta, (idpedido, idproducto, precioproducto, unidades))
            conexion.commit()
                
            #Una opcion para continuar o no
            opcion = input("¿Desea Continuar? Si/No ").lower()
            if opcion == "no":
                break
            else:
                continue
            
            
        
        
    except ValueError as e:
        print(fr.RED + f"Error al comprar un producto: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def Details(cursor, conexion):
    try:
        #Comprobar si Factura existe y si existe que lo elimine
        archivo = Path("Factura.txt")
        if archivo.exists():
            archivo.unlink()
        idcliente = input("Ingrese tú ID de cliente para hacerle una factura: ")

        # Consulta global de MySQL
        consulta = """
        SELECT 
            c.Nombre AS Cliente,
            c.ciudad AS Ciudad,
            c.tlf AS Telefono,
            p.idpedido AS PedidoID,
            prod.nombre AS Producto,
            d.unidades AS Unidades,
            d.precio AS PrecioUnidad,
            SUM(d.unidades * d.precio) AS PrecioTotalPedido
        FROM 
            cliente c
        INNER JOIN 
            pedido p ON c.idcliente = p.idcliente
        INNER JOIN 
            detalle d ON p.idpedido = d.idpedido
        INNER JOIN 
            producto prod ON d.idproducto = prod.idproducto
        WHERE 
            c.idcliente = %s
        GROUP BY 
            p.idpedido, c.idcliente, prod.idproducto, c.Nombre, c.ciudad, c.tlf, prod.nombre, d.unidades, d.precio
        ORDER BY 
            p.idpedido;
        """

     
        cursor.execute(consulta, (idcliente,))

        # Imprimir en terminal el resultado
        resultados = cursor.fetchall() 
        print("Resultados de la consulta:")
        for row in resultados:
            print(row)
        # Meter resultados en un array
        detalles_pedido = np.array(resultados)

        # Guardar los resultados en un archivo de texto
        with open("Factura.txt", "w") as archivo:
            for Cliente,Ciudad, Telefono, PedidoID, Producto, Unidades, PrecioUnidad, PrecioTotalPedido  in detalles_pedido:
                archivo.write(f"Cliente: {Cliente}, Ciudad: {Ciudad}, Teléfono: {Telefono}\n")
                archivo.write(f"Pedido ID: {PedidoID}, Producto: {Producto}, Unidades: {Unidades}, Precio Unidad: {PrecioUnidad}\n")
                archivo.write(f" Precio Total Pedido: {PrecioTotalPedido}\n")
                archivo.write("\n")
            archivo.close
    
    except ValueError as e:
        print(fr.RED + f"Error al detallar una compra: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)