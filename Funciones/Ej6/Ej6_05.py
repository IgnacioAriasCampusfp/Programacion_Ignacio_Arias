tareas = []




def ingresar_tareas():
    while True:
        tarea = input("¿Qué tarea quieres introducir? (escribe 'fin' para terminar): ")
        if tarea.lower() == "fin":
            break
        urgente = input("¿Es una tarea urgente? (True/False): ").lower()
        if urgente == "true":
            urgente = True
        else:
            urgente = False
        tareas.append({"Tarea": tarea, "Urgente": urgente})


def es_urgente(tarea):
    return tarea["Urgente"]


ingresar_tareas()


tareas_urgentes = list(filter(es_urgente, tareas))


if tareas_urgentes:
    print("\nTareas urgentes:")
    for tarea in tareas_urgentes:
        print(f"{tarea['Tarea']}")
else:
    print("\nNo hay tareas urgentes.")
