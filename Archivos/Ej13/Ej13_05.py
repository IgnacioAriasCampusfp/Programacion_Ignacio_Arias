import numpy as np

with open("matriz.txt", "w") as archivo:
    
    
    for i in range(1,4):
        n1 = np.random.randint(1,10)
        n2 = np.random.randint(1,10)
        n3 = np.random.randint(1,10)
        archivo.write(str(n1)+","+str(n2)+","+str(n3) + "\n")
    archivo.close
    
with open("matriz.txt", "r+") as archivo:
    lineas = archivo.readlines()
    matrices = np.array([list(map(int, linea.strip().split(','))) for linea in lineas])
    archivo.close
    
print(matrices)