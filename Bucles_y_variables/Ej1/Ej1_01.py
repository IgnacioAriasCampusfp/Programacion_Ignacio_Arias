n1 = input("Introduce el primer numero ")
n2 = input("Introduce el segundo numero ")
n1 = float(n1)
n2 = float(n2)
respuesta = input("¿Que operacion quieres hacer? suma, resta, multiplicacion o division ")

if respuesta == "suma":
    suma = n1 + n2
    print("El resultado de la suma es " , suma)
    
elif respuesta == "resta":
    resta = n1 - n2
    print("El resultado de la resta es " , resta) 
elif respuesta == "multiplicacion":
    multiplicacion = n1 * n2
    print("El resultado de la multiplicacion es " , multiplicacion)
elif respuesta == "division":
    if n2 == 0:
        print("Error no puede se puede divir en 0")
    else:
        division = n1 / n2
        print("El resultado de la division es " , division)

    
    
    