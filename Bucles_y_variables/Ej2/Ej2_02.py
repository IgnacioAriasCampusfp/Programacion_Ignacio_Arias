print("Introduce los numeros que quieras saber el promedio hasta que introduzcas 0 que se termina el programa")
contador = 0
numero = 0
numerosumado = 0
while True:
    numero = int(input("Que numero quieres sumar"))
    if numero!=0:
        numerosumado = numerosumado + numero
        print(f"la suma de tus numeros es {numerosumado}")
        contador +=1
    else:
        break
promedio = numerosumado / contador
print(f"Tu promedio es {promedio}")
        
        