
import random
respuestas = ["Piedra","Papel","Tijera"]
victoriasH = 0
victoriasM = 0



print( "\n \n ***************** \n Inicialización de Programa \n Ignacio Arias \n *****************")

####Inicialización del bucle####
while True:
    print("Elige 1-Piedra | 2-Papel | 3-Tijeras ")
    ####Obtención de la eleccion de la maquina####
    nmaquina = random.randint(1,3)
    
    
    respuesta = int(input("> "))
    print(f"Has elegido {respuestas[respuesta-1]}")
    print(f"La maquina ha elegido {respuestas[nmaquina-1]}")
    
    
    if respuesta == nmaquina:
        print("Habeis empatado Empate")
        victoriasM = 0
        victoriasH = 0
        
    elif respuesta != nmaquina:
        ####Secion de Victoria####
        if (respuestas[respuesta-1] == "Piedra" and respuestas[nmaquina-1] == "Tijera") or (respuestas[respuesta-1] == "Papel" and respuestas[nmaquina-1] == "Piedra") or (respuestas[respuesta-1] == "Tijera" and respuestas[nmaquina-1] == "Papel"):
            print("Has Ganado")
            victoriasM = 0
            victoriasH += 1
        
        ####Seccion de derrotas####
        elif (respuestas[respuesta-1] == "Tijera" and respuestas[nmaquina-1] == "Piedra") or (respuestas[respuesta-1] == "Piedra" and respuestas[nmaquina-1] == "Papel") or (respuestas[respuesta-1] == "Papel" and respuestas[nmaquina-1] == "Tijera"):
            print("Has Perdido") 
            victoriasH = 0
            victoriasM += 1
        
        if victoriasH>0:
            print(f"Llevas una racha de victorias de: {victoriasH}")
        elif victoriasM>0:
            print(f"Llevas una racha de derrotas de: {victoriasM}")
    
    ####Comprobacion de la racha de victorias tanto maquina o usuario####
    if victoriasH >= 3 or victoriasM >= 3:
        if victoriasH >= 3:
            print("Felicidades has ganado")
        elif victoriasM >= 3:
            print("Has perdido, mas suerte la proima vez")
        print("***************** \n Finalización del Programa \n *****************")
        break
            
            
        