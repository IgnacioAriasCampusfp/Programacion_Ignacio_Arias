from Funciones import DOW_categoria as dw


def Menu(cursor,conexion):
    try:
        while True:
            print("=== Gestión de Categorías ===\nSeleccione una opción:\n1. Crear nueva categoría\n2. Leer categorías existentes\n3. Actualizar una categoría\n4. Eliminar una categoría\n5. Salir")
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
                    print("Cerrando base de datos y saliendo del programa")
                    cursor.close()
                    conexion.close()
                    break
                case _:
                    print("Opción no valida")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    except ValueError as e:
        print(f"No has ingresado una opción valida: {e}")