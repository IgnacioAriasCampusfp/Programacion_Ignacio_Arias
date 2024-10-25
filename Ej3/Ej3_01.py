canciones = []

i=0

while True:
   
    check = input("Escribe nombre y escribe fin para terminar e imprimir las canciones ")
   
   
    if check == "fin":
        break
    else:
        canciones = canciones + [check]
       
print("Tu lista de canciones")
for check in canciones:
    print(i+1,check)
    i +=1
    
n_cancion = int(input("Ingresa el número de la canción que quieres reproducir: "))
i = n_cancion
print(canciones[i-1])
