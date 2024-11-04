''''
print("Primera Parte")
mi_nombre = "Nacho"
mi_edad = 22
print("Mi nombre es", mi_nombre)
print("Tengo", mi_edad, "años")


lado=5
area = lado + lado
print("El area del cuadrado es", area)

edad = 16
es_adulto = edad >= 18
print("Es adulto?", es_adulto)

#edad = input("Introduce tu edad: ")
#edad = int(edad)
#edad_futura = edad + 10
#print("En 10 años tendrás", edad_futura, "años")

print("Segunda parte")

a = 5 
b= 3
resultado = a + b
print(resultado)

a = 10
b = 4
resultado = a - b
print(resultado)

a = 6
b = 7
resultado = a * b
print(resultado)

a = 8
b = 2
resultado = a / b
print(resultado)

a = 9
b = 5
resultado = a // b
print(resultado)

a = 10
b = 3
resultado = a % b
print(resultado)

a = 2
b = 3
resultado = a ** b
print(resultado)

print ("Tercera parte Cadenas de texto")

nombre = "Juan"
apellido = "Perez"
nombre_completo = nombre + "" + apellido
print(nombre_completo)

frase = "Hola! "
repetida = frase * 3
print(repetida)

frase = "Python"
letra = frase[5]
print(letra)

frase = "Python"
longitud = len(frase)
print(longitud)

mi_lista = [1,2,3,4,5]
print(mi_lista)

mi_lista = ["manzana","banana"]
print(mi_lista)
mi_lista.append("cereza")
print(mi_lista)

mi_lista = ["banana", "manzana", "cereza"]
print(mi_lista [1])
mi_lista.remove("banana")
print(mi_lista[1])



incognita = input("Cual es")

if incognita == "a":
    b = input("Escribe b")
    b = int(b)
    c = input("Escribe c")
    c = int(c)
     
    from math import sqrt
    a = sqrt(c**2 - b**2)
    print (a)

'''
"""
temperatura = 30

if temperatura > 25:
    print("Hace calor")
else:
    print("Hace frio")

edad = 15
es_estudiante = True

if edad < 18 and es_estudiante:
    print("Es un estudiante menor de edad")
elif edad < 18 and not es_estudiante:
    print("Es menor de edad pero no es estudiante")
else:
    print("Es mayor de edad")
"""
"""Ejemplo 1"""
"""
for i in range(1, 11):
    print(i)
"""
"""Ejemplo 2"""
"""
numeros = [1, 2, 3, 4, 5]
suma = 0

for numero in numeros:
    suma += numero

print("La suma es", suma)

"""
"""Ejemplo 3"""
"""
for numero in range(1, 100):
    if numero % 7 == 0:
        print("El primer número divisible por 7 es", numero)
        break

"""
"""Ejemplo 4"""
"""
contador = 0
numero = 0

while contador < 5:
    if numero % 2 == 0:
        print(numero)
        contador += 1
    numero += 1
print(f"La cadena de pares es: {contador}")
"""

#Funciones
"""
def suma():
    suma = 2+3
    print(f"La suma es: {suma}")
    
def resta():
    resta = 2-3
    print(f"La resta es: {resta}")

def multiplica():
    multiplica = 2*3
    print(f"La multiplicacion es: {multiplica}")

def divide():
    division = 2/3
    print(f"La division es: {divide}")
    
######################

def sumapro(n1,n2):
    suma = n1+n2
    print(f"La suma de {n1} y de {n2} es: {suma}")



##############

n1 = int(input("dame n1 "))
n2 = int(input("dame n2 "))

sumapro(n1,n2)
"""
#Importar el Ej3_05 para obtener los def
"""
import Ej3_05

Ej3_05.restapro(n1,n2)
Ej3_05.dividepro(n1,n2)
Ej3_05.multipro(n1,n2)

resultadosuma = Ej3_05.sumapro2(n1,n2)
print(f"El resultado de sumapro2 es {resultadosuma}")
"""
"""
def espar(numero):
    if numero % 2==0:
        valor = True
    else:
        valor = False
    return valor

n1 = int(input("dame n1 "))
if espar(n1):
    print(f"El numero {n1} es par")
else:
    print(f"El numero {n1} es impar")
"""


"""

base= 5
altura=5
resultado = []
def area_triangulo():
    resultado.append( base*altura)
    print("El área del triángulo es", resultado)
   



area_triangulo()

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


resultado = es_par(8)
print("¿El número es par?", resultado)

def saludo_personalizado(nombre, hora_del_dia):
    if hora_del_dia == "mañana":
        print("¡Buenos días, " + nombre + "!")
    elif hora_del_dia == "tarde":
        print("¡Buenas tardes, " + nombre + "!")
    else:
        print("¡Buenas noches, " + nombre + "!")

saludo_personalizado("Laura", "tarde")

"""
def calculadora():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operacion = input("Ingresa la operación (+, -, *, /): ")


        if operacion == '+':
            print(f"Resultado: {num1 + num2}")
        elif operacion == '-':
            print(f"Resultado: {num1 - num2}")
        elif operacion == '*':
            print(f"Resultado: {num1 * num2}")
        elif operacion == '/':
            print(f"Resultado: {num1 / num2}")
        else:
            print("Operación no válida.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

calculadora()