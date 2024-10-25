asteriscos = " * "

print( "\n \n ***************** \n Inicialización de Programa \n Ignacio Arias \n *****************")
####Incializamos un bucle#####
while True:
    
    print("MENU \n 1- Cuadrado \n 2- Rectangulo \n 3- Salir  \n Dime tu opcion:" )
    selecion = int(input(">  "))
    ####Comprobar la seleción del usuario####
    if selecion == 1:
        print("Has seleccionado cuadrado")
        n1 = int(input("Dime la base del cuadrado: "))        
        ####Dibujo de un cuadrado con asteriscos####
        for i in range(1,n1+1):
            print(asteriscos*n1)
        ####Calcular Area y Perimetro####
        a = n1*n1
        print(f"El area del cuadrado es: {a}")
        perimetro = 4*n1
        print(f"El perimetro del cuadrado es: {perimetro}")
    elif selecion == 2:
        n1 = int(input("Dime la base del Rectangulo: "))
        n2 = int(input("Dime la altura del Rectangulo: "))
        ####Dibujo de un cuadrado con asteriscos####
        for i in range(1,n2+1):
            print(asteriscos*n1)
        ####Calcular Area y Perimetro####
        a = n1 * n2
        print(f"El area del rectangulo es: {a}")
        perimetro = 2*(n1+n2)
        print(f"El perimetro del cuadrado es: {perimetro}")
    elif selecion == 3:
        print("***************** \n Finalización del Programa \n *****************")
        break
    else:
        print("Eso no es una opción valida")