asignaturas = []
Asignatura ="Asignatura"
Notas = "Notas"

while True:
    asignatura = input("Introduce una asignatura o escribe fin: ")
    if asignatura != "fin":
        calificanion = int(input("Introduce una nota: "))
        asignaturas.append({Asignatura : asignatura, Notas: calificanion})
    else:
        break
print("Resumen de las asignaturas")


for asignaturas in asignaturas:
    
    print(asignaturas[Asignatura],": ",asignaturas[Notas])
    
total_notas = 0
num_asignaturas = len(asignaturas)

for asignatura in asignaturas:
    total_notas += asignatura[Notas]
    
if num_asignaturas > 0:
    promedio = total_notas / num_asignaturas
    print(f"El promedio de las notas es: {promedio}")