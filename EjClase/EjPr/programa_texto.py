import utilidades

texto = input("Introduce un texto: ")

print("Texto en mayuscula: ", utilidades.convertir_a_mayusculas(texto))
print("Texto en mayuscula: ", utilidades.convertir_a_minuscula(texto))
if utilidades.es_palidromo(texto):
    print("El texto es palídromo")
else:
    print("El texto no es un palíndromo")




