def generar_pares(n1,n2):
    contador = 0
    for numero in range(n1,n2+1):
       
        if numero % 2 == 0:
            contador +=1
    return contador
   

   
print(generar_pares(1,50))