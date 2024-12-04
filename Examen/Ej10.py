temperaturas = [15.5, 20.3, 18.2, 25.0, 30.5]
temperatura = 0

def convertir_a_fahrenheit(n1):
    temperatura = n1*1.8+32
    return temperatura

convert = list(map(convertir_a_fahrenheit,temperaturas))
print(convert)