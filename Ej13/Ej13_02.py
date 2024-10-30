import numpy as np 
from colorama import Fore as f
with open('temperaturas.txt', 'w') as archivo:
    for i in range(1,13):
        temperatura = input(f"Dime tu temperatura: ")
        archivo.write(temperatura + " \n")
    archivo.close


        
with open('temperaturas.txt', 'r+') as archivo:
    lineas = archivo.readlines()
    array1 = np.array([int(linea.strip()) for linea in lineas])
    archivo.close
promedio = np.mean(array1)
maxima = np.max(array1)
minima = np.min(array1)
print(f.BLUE+ f"El promedio de temperatura es: {promedio:.2f}°C")
print(f"La maxima de temperatura es: {maxima}°C")
print(f"La minima de temperatura es: {minima}°C")
    

    
    