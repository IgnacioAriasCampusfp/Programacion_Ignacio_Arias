def convertir_a_mayusculas(texto):
    return texto.upper()

def convertir_a_minuscula(texto):
    return texto.lower()

def es_palidromo(texto):
    texto.replace("","").lower()
    return texto == texto[::-1]

