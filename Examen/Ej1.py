numeros = [5, 15, 25, 35, 45]
suma = 0

for numero in numeros:
    suma += numero

promedio = suma / len(numeros)

print(promedio)
array = []

for numero in numeros:
    if numero>promedio:
        array.append(numero)
        
print(array)

