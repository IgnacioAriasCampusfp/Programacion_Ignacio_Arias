itinerario = ("Madrid", "Barcelona", "Sevilla", "Valencia")

print("Itinerario de viaje: ")
for i in range(len(itinerario)):
    print(i+1, itinerario[i])
    
posicion = int(input("Ingresa la posición para saber qué ciudad visitarás: "))
print(f"En la posición {posicion} visitaras {itinerario[posicion-1]}")