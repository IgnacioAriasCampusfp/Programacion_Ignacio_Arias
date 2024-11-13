with open('notas.txt', 'w') as archivo:
    archivo.close
with open('notas.txt', 'a') as archivo:
    archivo.write(input("Escribe tus notas\n"))
    archivo.write(input("Escribe tus notas\n"))
    archivo.write(input("Escribe tus notas\n"))
    archivo.close
    