n1 = input("¿Que numero quieres sumar desde el 1 hasta el tuyo? ")
suma = 0
n1 = int(n1)
for i in range(1,n1+1):
    suma = suma + i
    print("La suma de estos numeros es: ", suma)