def contar_vocales(cadena):
    contador = 0
    for cadena in cadena:
        if cadena in ("aeiou"):
            contador = contador + 1
    return contador

cadena = input("Escribe la frase que quieras contar vocales: ")
print(contar_vocales(cadena))