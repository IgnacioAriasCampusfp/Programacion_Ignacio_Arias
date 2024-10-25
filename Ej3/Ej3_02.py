
listdic = []

while True:
    Continuar = input("Si quiere continuar escribe si, si no escribe fin: " )
    if Continuar=="fin":
        break
    else:
        listdic.append({"Nombre": input("Escribe el nombre: "), "Tlf" : input("Introduce un numero de telefono: ")})

print("Tus contactos: ")

for listdic in listdic:
    
    print(listdic["Nombre"],": ",listdic["Tlf"])

nombreB = input("Que usuario deseas buscar ")

for listdic in listdic:
    if listdic == nombreB:
        print(f"el numero de telefono de {nombreB} es: ", listdic["Tlf"])
    else:
        print()
