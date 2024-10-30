import numpy as np 

with open('notas_estudiantes.txt', 'w') as archivo:
    archivo.write("89,90,91 \n")
    archivo.write("70,71,72 \n")
    archivo.write("50,51,52 \n")
    archivo.write("10,15,25 \n")
    archivo.write("100,64,76 \n")
    archivo.close

with open("notas_estudiantes.txt", "r+") as archivo:
    lineas = archivo.readlines()

    calificaciones = np.array([list(map(int, linea.strip().split(','))) for linea in lineas])
    archivo.close
    
promedio = np.mean(calificaciones, axis=1)
promedio = np.round(promedio)
promedio_estudiantes = np.mean(calificaciones)
promedio_estudiantes = np.round(promedio_estudiantes)

print(promedio)
print(promedio_estudiantes)
