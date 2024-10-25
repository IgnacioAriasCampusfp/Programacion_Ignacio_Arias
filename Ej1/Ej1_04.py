palabra = input("¿Que palabra quieres saber cuantas vocales tiene? ")
i = 0
contador = 0
cpalabra = len(palabra)
while i <= cpalabra:
    
    letra = palabra[i]
    letra = str(letra)
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"  :
       
        contador = contador + 1   
        i = i + 1
       
    else:
        i = i + 1
    if i >= cpalabra:
            break
    
print(contador)
        
