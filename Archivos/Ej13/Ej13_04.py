import numpy as np

with open ("valores.txt","w") as archivo:
    for i in range(1,16):
        n_random = np.random.randint(-50,50)
        archivo.write(f"{n_random}\n")
    archivo.close

with open("valores.txt","r+") as archivo:
    lineas = archivo.readlines()
    numeros = np.array([int(linea.strip()) for linea in lineas])
    positivos = numeros[numeros>=0]
    archivo.close
    
with open("valores_positivos.txt","w") as archivo:
    archivo.write(str(positivos))
    archivo.close


with open("valores_positivos.txt","r+") as archivo:
    lineas = archivo.readlines()
    numeros_positivos = np.array([linea.strip() for linea in lineas])
    archivo.close
    
print(numeros_positivos)