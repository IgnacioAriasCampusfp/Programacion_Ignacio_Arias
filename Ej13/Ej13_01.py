import numpy as np 


with open('numeros.txt', 'w') as archivo:
    for i in range(0,11):
        n_random = np.random.randint(1,100)
        archivo.write(f'{n_random}\n')
    
    archivo.close

with open('numeros.txt', 'r+') as archivo:
    lineas = archivo.readlines()
    
    array1 = np.array([linea.strip() for linea in lineas])
print(array1)
        