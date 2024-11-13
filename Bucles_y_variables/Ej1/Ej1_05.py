n1 = 0
import random
n1 = random.randint(1,100)

while True:
    n2 = input("¿Dime un numero entre 1 hasta el 100?")
    n2 = int(n2)
    if n2 == n1:
        print("Felicidades has acertado")
        break
    elif n2 < n1:
        print("Tu numero es menor que el secreto")
    elif n2 > n1:
        print("Tu numero es mayor que el secreto")