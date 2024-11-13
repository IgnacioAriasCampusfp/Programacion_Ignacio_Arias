import numpy as np


def cargar_partida(tablero,posicionb1,posicionb2,posicionb3):
    
    tablero = np.zeros((20, 20), dtype=int)  # Reiniciar el tablero por si acaso
    try:
        with open("partida_comenzada.txt", "r") as archivo:
            # Leer las primeras 20 filas del tablero
            
            for i in range(20):
                fila = archivo.readline().strip()
                if fila == "":  # Si hay una línea vacía, muestra un mensaje de error
                    raise ValueError(f"La fila {i} está vacía.")
                fila_lista = list(map(int, fila.split()))
                if len(fila_lista) != 20:  # Si la fila no tiene 20 elementos
                    raise ValueError(f"La fila {i} no tiene 20 elementos: {fila_lista}")
                tablero[i] = np.array(fila_lista)
            
            # Leer las posiciones de los tres elementos
            for i in range(21,22):  # Suponiendo que lees las líneas 21 y 22
                fila = archivo.readline().strip().split()  # Ahora split() divide correctamente la línea
                posicionb1 = np.array([list(map(int, fila))])  # Convierte cada elemento de la fila en entero
            for i in range(23,25):  # Suponiendo que lees las líneas 21 y 22
                fila = archivo.readline().strip().split()  # Ahora split() divide correctamente la línea
                posicionb2 = np.array([list(map(int, fila))])  # Convierte cada elemento de la fila en entero
           
            
            #posicionb3 = np.array(list(map(int, archivo.readline().strip().split())))

        print("Partida cargada.")
    
    except FileNotFoundError:
        print("No hay partida guardada. Generando nueva partida.")
    except ValueError as e:
        print(f"Error al cargar la partida: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")