coches = []
def ingresar_coches():
    while True:
        coche = input("¿Qué Vehiculo quieres intorducir? (escribe 'fin' para terminar): ")
        if coche.lower() == "fin":
            break
        revision = input("¿Ha pasado la ITV? (True/False): ").lower()
        if revision == "true":
            revision = True
        else:
            revision = False
        coches.append({"Vehiculo": coche, "ITV": revision})




def ITV(coche):
    return coche["ITV"]


ITV()


cochesitv = list(filter(ITV, coches))




if cochesitv:
    print("Coches que han pasado la ITV:")
    for coche in cochesitv:
        print(f"{coche['Vehiculo']}")
else:
    print("No se han ingresado coches.")
