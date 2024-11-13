import numpy as np 

n_random = np.random.randint(1,100,size=10)

with open('numeros.txt', 'w') as archivo: 
    archivo.write(f'{n_random}\n') 
    archivo.close

with open('numeros.txt', 'r+') as archivo:
    lineas = archivo.readlines()
    
    array1 = np.array([linea.strip() for linea in lineas])
print(array1)
        