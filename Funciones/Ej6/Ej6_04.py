libros = []


def ingresar_libros():
    while True:
        libro = input("¿Qué libro quieres introducir? (escribe 'fin' para terminar): ")
        if libro.lower() == "fin":
            break
        categoria = input("¿A qué categoría pertenece el libro? (ej. novela, ensayo, poesía): ").lower()
        libros.append({"Libro": libro, "Categoria": categoria})
       
def es_novela(libro):
    return libro["Categoria"] == "novela"


ingresar_libros()


libros_novela = list(filter(es_novela, libros))


if libros_novela:
    print("\nLibros de la categoría 'novela':")
    for libro in libros_novela:
        print(f"{libro['Libro']}")
else:
    print("\nNo se han ingresado libros de la categoría 'novela'.")
