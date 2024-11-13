from colorama import Fore as fr

def Create(cursor, conexion):
    try:
        idcliente = input(fr.LIGHTCYAN_EX + "Ingrese el ID del cliente: " + fr.RESET)
        cia = input(fr.LIGHTCYAN_EX + "Ingrese el cia del cliente: " + fr.RESET).strip()
        contacto = input(fr.LIGHTCYAN_EX + "Ingrese el nombre del cliente: " + fr.RESET)
        cargo = input(fr.LIGHTCYAN_EX + "Ingrese el cargo del cliente: " + fr.RESET)
        direccion = input(fr.LIGHTCYAN_EX + "Ingrese la direccion del cliente: " + fr.RESET)
        ciudad = input(fr.LIGHTCYAN_EX + "Ingrese la ciudad del cliente: " + fr.RESET)
        region = input(fr.LIGHTCYAN_EX + "Insgrese la región del cliente: "+ fr.RESET)
        cp = int(input(fr.LIGHTCYAN_EX +"Ingrese el codigo postal del cliente: "+ fr.RESET))
        pais = input(fr.LIGHTCYAN_EX +"Ingrese el pais del cliente: "+ fr.RESET)
        tlf = int(input(fr.LIGHTCYAN_EX +"Ingrese el telefono del cliente: "+ fr.RESET))
        fax = int(input(fr.LIGHTCYAN_EX +"Ingrese el numero de FAX del cliente: " + fr.RESET))
        
        consulta = """INSERT INTO cliente (idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(consulta, (idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax))
        conexion.commit()
        print(fr.GREEN + f"El cliente '{cia}' ha sido creado con éxito." + fr.RESET)
        
       
        
        print(fr.CYAN + "Listado de Clientes:" + fr.RESET)
        consulta = "SELECT * FROM cliente ORDER BY idcliente;"
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        for idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax in resultados:
            print(fr.YELLOW + f"--->ID: {idcliente} Cia: {cia} Contacto: {contacto}, Cargo: {cargo},\nDireccion: {direccion} Ciudad: {ciudad} Region: {region} Cp: {cp} Pais: {pais} Tlf: {tlf} Fax: {fax}" + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al crear un cliente: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
        
def List(cursor, conexion):
    try:
        consulta = "SELECT * FROM cliente;"
        cursor.execute(consulta)
        
        print(fr.CYAN + "Listado de Clientes:" + fr.RESET)
        resultados = cursor.fetchall()
        for idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax in resultados:
            print(fr.YELLOW + f"--->ID: {idcliente} Cia: {cia} Contacto: {contacto}, Cargo: {cargo},\nDireccion: {direccion} Ciudad: {ciudad} Region: {region} Cp: {cp} Pais: {pais} Tlf: {tlf} Fax: {fax}" + fr.RESET)
    except ValueError as e:
        print(fr.RED + f"Error al listar clientes: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def Actu(cursor, conexion):
    try:
        idcliente = input(fr.LIGHTCYAN_EX + "Ingrese el ID del cliente: " + fr.RESET)
        cia = input(fr.LIGHTCYAN_EX + "Ingrese el cia del cliente: " + fr.RESET).strip()
        contacto = input(fr.LIGHTCYAN_EX + "Ingrese el nombre del cliente: " + fr.RESET)
        cargo = input(fr.LIGHTCYAN_EX + "Ingrese el cargo del cliente: " + fr.RESET)
        direccion = input(fr.LIGHTCYAN_EX + "Ingrese la direccion del cliente: " + fr.RESET)
        ciudad = input(fr.LIGHTCYAN_EX + "Ingrese la ciudad del cliente: " + fr.RESET)
        region = input(fr.LIGHTCYAN_EX + "Insgrese la región del cliente: "+ fr.RESET)
        cp = int(input(fr.LIGHTCYAN_EX +"Ingrese el codigo postal del cliente: "+ fr.RESET))
        pais = input(fr.LIGHTCYAN_EX +"Ingrese el pais del cliente: "+ fr.RESET)
        tlf = int(input(fr.LIGHTCYAN_EX +"Ingrese el telefono del cliente: "+ fr.RESET))
        fax = int(input(fr.LIGHTCYAN_EX +"Ingrese el numero de FAX del cliente: " + fr.RESET))
        
        consulta = """
        UPDATE cliente SET cia = %s, contacto = %s, cargo = %s, direccion = %s, ciudad = %s, region = %s, cp = %s, pais = %s, tlf = %s, fax = %s WHERE idcliente = %s
        """
        cursor.execute(consulta, (cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax, idcliente))
        conexion.commit()
        print(fr.GREEN + f"El cliente '{cia}' ha sido actualizada con éxito." + fr.RESET)
        
        print(fr.CYAN + "Listado de Clientes Actualizado:" + fr.RESET)
        consulta = "SELECT * FROM cliente ORDER BY idcliente;"
        cursor.execute(consulta)
        
        resultados = cursor.fetchall()
        for idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax in resultados:
            print(fr.YELLOW + f"--->ID: {idcliente} Cia: {cia} Contacto: {contacto}, Cargo: {cargo},\nDireccion: {direccion} Ciudad: {ciudad} Region: {region} Cp: {cp} Pais: {pais} Tlf: {tlf} Fax: {fax}" + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al actualizar un cliente: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)

def Delete(cursor, conexion):
    try:
        idcliente = input(fr.LIGHTCYAN_EX + "Ingrese el ID del cliente que desea eliminar: " + fr.RESET)
        
        consulta = "DELETE FROM cliente WHERE idcliente = %s"
        cursor.execute(consulta, (idcliente,))
        conexion.commit()
        print(fr.GREEN + f"El cliente con ID '{idcliente}' ha sido eliminado con éxito." + fr.RESET)
        
    except ValueError as e:
        print(fr.RED + f"Error al eliminar un cliente: {e}" + fr.RESET)
    except Exception as e:
        print(fr.RED + f"Ocurrió un error inesperado: {e}" + fr.RESET)
