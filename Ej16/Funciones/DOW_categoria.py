

def Create(cursor,conexion):
    try:
        idproducto = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ").strip()
        idcategoria = int(input("Ingrese el ID de la categoría: "))
        medida = input("Insertar medida del producto Ej: '10 cajas x 20 bolsas' : ")
        precio = int(input("Precio del producto: "))
        stock = int(input("Cuanto de stock hay: "))
        
        
        consulta = """INSERT INTO producto (idproducto , nombre, idcategoria, medida, precio, stock) VALUES (%s, %s,%s, %s,%s, %s)"""
        cursor.execute(consulta,(idproducto,nombre,idcategoria,medida,precio,stock))
        conexion.commit()
        print(f"El producto '{nombre}' ha sido creada con éxito.")
        
        print("Listado de Categorías:")
        consulta = """
        SELECT*FROM producto
        ORDER BY idproducto;
        """
        cursor.execute(consulta)
        # Obtener y mostrar los resultados
        resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        for idproducto,nombre,idcategoria,medida,precio,stock in resultados:
            print(f"IDproducto: {idproducto}, Nombre: {nombre}, IdCategoria: {idcategoria}, Medida: {medida}, Precio: {precio}, Stock: {stock}")
        
    except ValueError as e:
        print(f"Error al crear una nueva categoria: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        
def List(cursor,conexion):
    try:
        consulta = """
        SELECT *
        FROM producto;
        """
        cursor.execute(consulta)
        # Obtener y mostrar los resultados
        resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        for idproducto,nombre,idcategoria,medida,precio,stock in resultados:
            print(f"IDproducto: {idproducto}, Nombre: {nombre}, IdCategoria: {idcategoria}, Medida: {medida}, Precio: {precio}, Stock: {stock}")
        
    except ValueError as e:
        print(f"Error al crear una actualizar categoria: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def Actu(cursor,conexion):
    try:
        idproducto = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ").strip()
        idcategoria = int(input("Ingrese el ID de la categoría: "))
        medida = input("Insertar medida del producto Ej: '10 cajas x 20 bolsas' : ")
        precio = int(input("Precio del producto: "))
        stock = int(input("Cuanto de stock hay: "))
        consulta = """
    UPDATE producto SET nombre = %s, idcategoria = %s, medida = %s, precio = %s, stock = %s WHERE idnombre = %s"""
        
        cursor.execute(consulta,(nombre,idcategoria,medida,precio,stock,idproducto))
        conexion.commit()
        print(f"El producto '{nombre}' ha sido actualizada con éxito.")
        
        print("Listado de Categorías Actualizada:")
        consulta = """
        SELECT*FROM producto
        ORDER BY idproducto;
        """
        cursor.execute(consulta)
        # Obtener y mostrar los resultados
        resultados = cursor.fetchall()  # Obtiene todos los resultados de la consulta
        for idproducto,nombre,idcategoria,medida,precio,stock in resultados:
            print(f"IDproducto: {idproducto}, Nombre: {nombre}, IdCategoria: {idcategoria}, Medida: {medida}, Precio: {precio}, Stock: {stock}")
        
        
    except ValueError as e:
        print(f"Error al crear una actualizar categoria: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")



def Delete(cursor,conexion):
    try:
        idproducto = int(input("Ingrese el ID del producto que quieras eliminar: "))
        
        consulta = "DELETE FROM producto WHERE idproducto = %s"
        cursor.execute(consulta, (idproducto,))
        conexion.commit()
        print(f"El producto '{idproducto}' ha sido eliminada con éxito.")
        
        
    except ValueError as e:
        print(f"Error al crear una nueva categoria: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")