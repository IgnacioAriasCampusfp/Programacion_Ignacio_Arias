def guardar_partida(tablero,posicionb1,posicionb2,posicionb3):
    with open("partida_comenzada.txt", "w") as archivo:
        for fila in tablero:
            archivo.write(" ".join(map(str, fila)) + "\n")
        for fila in posicionb1+1:
            archivo.write(" ".join(map(str, fila)) + "\n")
        for fila in posicionb2+1:
            archivo.write(" ".join(map(str, fila)) + "\n")
        for fila in posicionb3+1:
            archivo.write(" ".join(map(str, fila)) + "\n")
    print("Partida guardada.")