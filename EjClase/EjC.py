'''Ejercicio 1'''
'''
edad =  input("Que edad tienes ")
edad = int(edad)

if edad<5:
    print("Tienes la entrada gratis")
elif edad>=5 or edad<=12:
    print("La entrada te cuesta 5 euros")
elif edad>=13 or edad<=17:
    print("La entrada te cuesta 7 euros")    
elif edad>=18:
    print("La entrada te cuesta 10 euros")  
   ''' 
"""Ejercicio 2"""
"""
nota = input("¿Que nota tienes?")
nota = int(nota)
match nota:
    case nota if nota>=90:
        print("Tienes una A")
    case nota if nota>=80 and nota<90:
        print("Tienes una B")
    case nota if nota>=70 and nota<80:
        print("Tienes una C")
    case nota if nota>=60 and nota<70:
        print("Tienes una D")
    case nota if nota<60:
        print("Tienes una F")
"""
"""Ejercicio 3"""
'''
dia = input("Que dia de la semana es en numeros ")
dia = int(dia)
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("No esta permitido ese numero")

'''
'''Ejercicio 4'''
"""
edad = int(input("Que edad tienes? "))
idioma = input("Que idioma quieres ") 

if edad<12:
    print("Eres un niño")
    
elif edad>=12 and edad<=17:
    print("Eres un Adolescente")
    
elif edad>=18 and edad<=59:
    print("Eres un Adulto")
    
elif edad>=60:
    print("Eres un Adulto mayor")
    
match idioma:
        case "es":
            print("Has selecionado el español")
        case "en":
            print("You have selected English")
        case "fr":
            print("Vous avez sélectionné le français")
        case _:
            print("Lenguaje no soportado")
"""
"""Ejercicio 5"""
"""
vehiculo = input("¿Que vehiculo tienes? ")
color = input("¿De que color lo tienes? ")

if vehiculo=="coche":
    print("Tu vehiculo es un coche ")
elif vehiculo=="moto":
    print("Tu vehiculo es una moto")
elif vehiculo== "bicicleta":
    print("Tu vehiculo es una bicicleta")
else:
    print("Vehiculo no soportado")
match color:
    case "rojo":
        print("Has seleccionado color rojo")
    case "verde":
        print("Has seleccionado color verde")
    case "azul":
        print("Has seleccionado color azul")
    case _:
        print("Color no soportado")
"""

"""Ejercicios Bucle"""
"""Ejercicio 1"""
"""
numero = int(input("Dame un numero entero positivo "))
contador = 0
if numero >= 0:
    for i in range(1, numero):
        if i % 2 == 0:
            contador += 1
       
    print("La cantidad de numeros pares es: ", contador)
else:
    print("No es un numero positivo")

"""
"""Ejercicio 2"""
""" 
print("Debes introducir numeros positivos, si introduces un numero negativo se termina la operacion")
suma = 0
while True:
    numero = int(input("Introduce un numero"))
    if numero>=0:
        suma = suma + numero
    elif numero < 0:
        break
print("Tu suma final es: ",suma)
"""
"""Ejercicio 3"""
"""
n1 = int(input("Dime el numero que debo multiplicar: "))
n2 = int(input("Cuantas veces lo multiplico: "))
resultado= 0
for i in range(1,n2+1):
    resultado= 0
    resultado = n1*i
    print(n1, "x", i, " es igual a ", resultado)
"""
"""Ejercicio 4"""
"""
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
"""
"""Ejercicio 5"""
"""
palabra = input("Introduce la palabra que quieres saber cuantas vocales tienes: ")
contador = 0

for i in range (len(palabra)):
    letra = palabra[i]
    if letra in ("aeiou"):
        contador += 1
   # if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    #    contador += 1
print(f"La palabra {palabra} tiene {contador} vocales")
"""