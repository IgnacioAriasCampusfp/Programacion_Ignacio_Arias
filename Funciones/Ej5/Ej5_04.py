numeros = [10.2,22.84,15.49,82.51]

def redondear(redondeo):
    redondeo = round(redondeo)
    return redondeo
redondeohecho = list(map(redondear,numeros))
print(redondeohecho)