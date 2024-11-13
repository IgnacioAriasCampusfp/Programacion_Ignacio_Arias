from colorama import Fore as fr

def Create(cursor, conexion):
    try:
        idproducto = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID del producto: " + fr.RESET))
        nombre = input(fr.LIGHTCYAN_EX + "Ingrese el nombre del producto: " + fr.RESET).strip()
        idcategoria = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID de la categoría: " + fr.RESET))
        medida = input(fr.LIGHTCYAN_EX + "Insertar medida del producto Ej: '10 cajas x 20 bolsas': " + fr.RESET)
        precio = float(input(fr.LIGHTCYAN_EX + "Precio del producto: " + fr.RESET))
        stock = int(input(fr.LIGHTCYAN_EX + "Cuanto de stock hay: " + fr.RESET))
        
        consulta = """INSERT INTO producto (idproducto, nombre, idcategoria, medida, precio, stock) VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(consulta, (idproducto, nombre, idcategoria, medida, precio, stock))
        conexion.commit()
        print(fr.GREEN + f"El producto '{nombre}' ha sido creado con éxito." + fr.RESET)
        
        print(fr.CYAN + "Listado de Productos:" + fr.RESET)
        consulta = "SELECT * FROM producto ORDER BY idproducto;"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        for idproducto, nombre, idcategoria, medida, precio, stock in resultados:
            print(f"{fr.YELLOW}IDproducto: {idproducto}, Nombre: {nombre}, IdCategoria: {idcategoria}, Medida: {medida}, Precio: {precio}, Stock: {stock}{fr.RESET}")
        
    except ValueError as e:
        print(fr.RED + f"Error al crear un nuevo producto: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def List(cursor, conexion):
    try:
        consulta = "SELECT * FROM producto;"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        print(fr.CYAN + "Listado de Productos:" + fr.RESET)
        for idproducto, nombre, idcategoria, medida, precio, stock in resultados:
            print(f"{fr.YELLOW}IDproducto: {idproducto}, Nombre: {nombre}, IdCategoria: {idcategoria}, Medida: {medida}, Precio: {precio}, Stock: {stock}{fr.RESET}")
        
    except ValueError as e:
        print(fr.RED + f"Error al listar productos: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def Actu(cursor, conexion):
    try:
        idproducto = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID del producto: " + fr.RESET))
        nombre = input(fr.LIGHTCYAN_EX + "Ingrese el nombre del producto: " + fr.RESET).strip()
        idcategoria = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID de la categoría: " + fr.RESET))
        medida = input(fr.LIGHTCYAN_EX + "Insertar medida del producto Ej: '10 cajas x 20 bolsas': " + fr.RESET)
        precio = float(input(fr.LIGHTCYAN_EX + "Precio del producto: " + fr.RESET))
        stock = int(input(fr.LIGHTCYAN_EX + "Cuanto de stock hay: " + fr.RESET))
        
        consulta = """
        UPDATE producto SET nombre = %s, idcategoria = %s, medida = %s, precio = %s, stock = %s WHERE idproducto = %s
        """
        cursor.execute(consulta, (nombre, idcategoria, medida, precio, stock, idproducto))
        conexion.commit()
        print(fr.GREEN + f"El producto '{nombre}' ha sido actualizado con éxito." + fr.RESET)
        
        print(fr.CYAN + "Listado de Productos Actualizado:" + fr.RESET)
        consulta = "SELECT * FROM producto ORDER BY idproducto;"
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        for idproducto, nombre, idcategoria, medida, precio, stock in resultados:
            print(f"{fr.YELLOW}IDproducto: {idproducto}, Nombre: {nombre}, IdCategoria: {idcategoria}, Medida: {medida}, Precio: {precio}, Stock: {stock}{fr.RESET}")
        
    except ValueError as e:
        print(fr.RED + f"Error al actualizar un producto: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def Delete(cursor, conexion):
    try:
        idproducto = int(input(fr.LIGHTCYAN_EX + "Ingrese el ID del producto que quieres eliminar: " + fr.RESET))
        
        consulta = "DELETE FROM producto WHERE idproducto = %s"
        cursor.execute(consulta, (idproducto,))
        conexion.commit()
        print(fr.GREEN + f"El producto con ID '{idproducto}' ha sido eliminado con éxito." + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al eliminar un producto: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
