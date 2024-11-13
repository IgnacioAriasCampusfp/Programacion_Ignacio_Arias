monstruos = { 'vampiro': 3, 'momia': 2, 'bruja': 4, 'esqueleto': 1, 'fantasma': 5 } 
objetos = ['estaca', 'poción mágica', 'hechizo']
capturas = 0

import random


def Captura(capturas):
    print("¡Bienvenido a la caza de monstruos de Halloween!")
    while True:
        intentos = 3
        monstruo = random.choice(list(monstruos.keys()))     
        print(f"Un {monstruo} ha aparecido con dificultad {monstruos[monstruo]}")
        while True:
            if intentos == 0:
                break
            else:
                print(f"Tienes {intentos} intentos restantes")
                print(f"Elige un objeto para intentar capturar al vampiro: {objetos}")
                seleccion = input(f"Escribe el nombre del objeto: \n>").lower()
                if seleccion == "estaca" or seleccion == "pocion magica" or seleccion == "hechizo":
                    nivel = random.randint(1,5)
                    if nivel == monstruos[monstruo]:
                        print(f"¡Has capturado al {monstruo} con un/a {seleccion}!")
                        capturas+=1
                        break
                        
                        
                    else:
                        print(f"Fallaste al intentar capturar al {monstruo} con un/a {seleccion}.")
                        intentos -=1
                else:
                    print("No existe ese objeto")
        
        salir = input("¿Deseas continuar? si/no \n>")
        if salir == "si":
            print("Seguimos la caza de mounstros")
        else:
            return capturas
            

def capturados(capturas):
    print(f"Has capturado {capturas}")
       
capturas = Captura(capturas)

capturados(capturas)