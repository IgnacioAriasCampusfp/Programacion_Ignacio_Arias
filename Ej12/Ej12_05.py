with open('diario.txt', 'w') as archivo:
    archivo.write('Buenas querido diario hoy me han detectado cancer :)\n')

    archivo.close
    
with open('diario.txt', 'a') as archivo:
    archivo.write(input("Texto\n"))
    archivo.close
    
with open('diario.txt', 'r+') as archivo:
    contenido = archivo.read()
    print(contenido)