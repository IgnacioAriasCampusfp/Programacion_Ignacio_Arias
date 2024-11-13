productos = []

def ingresar_productos():
    while True:
        alimento = input("¿Qué producto deseas introducir? (escribe 'fin' para terminar): ")
        if alimento.lower() == "fin":
            break
        perecedero = input("¿Es perecedero? (True/False): ").lower() == "true"
        productos.append({"Nombre": alimento, "Perecedero": perecedero})

def es_perecedero(producto):
    return producto["Perecedero"]

ingresar_productos()

alimentos_perecederos = list(filter(es_perecedero, productos))

if alimentos_perecederos:
    print("Productos perecederos:")
    for producto in alimentos_perecederos:
        print(f"{producto['Nombre']}")
else:
    print("No se han ingresado productos perecederos.")