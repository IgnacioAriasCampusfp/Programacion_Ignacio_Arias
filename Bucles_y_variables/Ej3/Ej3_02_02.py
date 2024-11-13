dic={}
while True:
    nombre = input("Introduce un nombre o escribe fin: ")
    if nombre != "fin":
        contactos = int(input("Introduce un numero de telefono: "))
        dic[nombre]= contactos
        dic = {nombre,contactos}
    else:
        break

print(dic)
nombreb = input("Que nombre deseas buscar: ")
nombre = nombreb
print(f"El numero de telefono de {nombre} es {dic[nombre]}")

