palabras = ["Chocolate", "Platano", "Awacate"]

def longitudes(palabra):
    return len(palabra)

longitud = list(map(longitudes,palabras))
print(longitud)