with open('alumnos.txt', 'w') as archivo:
    archivo.write('Juan\n')
    archivo.write('Pedro\n')
    archivo.write('Alberto\n')
    archivo.write('Pablo\n')
    archivo.write('Alex\n')
    archivo.close

with open('alumnos.txt', 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())
        
