edades = [14, 21, 18, 17, 30, 25]

def es_mayor_de_edad(n1):
    return n1>=18

mayor = list(filter(es_mayor_de_edad,edades))

print(mayor)