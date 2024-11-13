empleados = []




def ingresar_empleados():
    while True:
        empleado = input("¿Qué empleado quieres intorducir? (escribe 'fin' para terminar): ")
        if empleado.lower() == "fin":
            break
        activo = input("¿Esta activo? (True/False): ").lower()
        if activo == "true":
            activo = True
        else:
            activo = False
        empleados.append({"Nombres": empleado, "Activo": activo})


def activo(empleado):
    return empleado["Activo"]


ingresar_empleados()


empleados_activos = list(filter(activo, empleados))




if empleados_activos:
    print("Empleados activos:")
    for empleado in empleados_activos:
        print(f"{empleado['Nombres']}")
else:
    print("No se han empleados activos.")
