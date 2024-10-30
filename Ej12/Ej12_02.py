with open('frase.txt', 'w') as archivo:
    archivo.write('Vida antes que muerte, viaje antes que destino, fuerza antes que debilidad ')

    archivo.close
with open('frase.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
    archivo.close
    