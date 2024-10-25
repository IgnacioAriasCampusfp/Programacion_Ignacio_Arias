movimientosr = []
movimientosi = []

print( "\n \n ***************** \n Inicialización de Programa \n Ignacio Arias \n *****************")

saldo = float(input("Saldo inicial \n > "))
####Incializamos un bucle#####
while True:
    print("MENU \n 1- Ingresar dinero \n 2- Retirar dinero \n 3- Mostrar saldo \n 4- Estadisticas \n 5- Salir \n Dime tu opcion:" ) 
    selecion = int(input(">  "))
    ####Comprobar la seleción del usuario####
    if selecion == 1:       
        ingresar = float(input("Dinero que quieres ingresar \n > "))
        if ingresar < 0:
            print("***No puede se puede ingresar numeros negativos***")
        else:
            ####Hacer sumas de saldo y meter movimientos####
            saldo =  saldo + ingresar
            movimientosi.append(ingresar)
            print(f"Has ingresado: {ingresar}. Tu nuevo saldo es: {saldo}")
        
    elif selecion == 2:
        retirar = float(input("Dinero que quieres retirar \n > "))
        if retirar < 0:
            print("***No puede se puede ingresar numeros negativos***")
        else:
            if retirar > saldo:
                print("***No puedes retirar más dinero del que tienes***")
            else:
                ####Hacer restas de saldo y meter movimientos####
                saldo = saldo - retirar
                movimientosr.append(retirar)
                print(f"Has retirado: {retirar}. Tu nuevo saldo es: {saldo}")
        
    elif selecion == 3:
        print(f"Tu saldo actual es: {saldo}")
    elif selecion == 4:
        ####Comprobar las listas de ingresar y restas en un bucle for####
        print("Tus movimientos en ingresos:")
        for movimientosi in movimientosi:
            print(f"> {movimientosi}€")
        print("Tus movimientos en retirar:")
        for movimientosr in movimientosr:
            print(f"> -{movimientosr}€")
    elif selecion == 5:
        print("***************** \n Finalización del Programa \n *****************")
        break
    else:
        print("Esa no es una opcion valida")
