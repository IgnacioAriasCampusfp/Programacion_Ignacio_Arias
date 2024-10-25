numeros = [4, 9, 16, 25, 1, 7, 12]

def mayorque10(n):
    return n > 10

numerosmayores = filter(mayorque10,numeros)
print(list(numerosmayores))