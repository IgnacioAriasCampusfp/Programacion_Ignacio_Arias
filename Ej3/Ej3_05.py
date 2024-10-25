"""
pedido = []
total_pagar = 0
calorias_totales = 0

menu = {
    "Café": (1.5, 50),
    "Té": (1.0, 0),
    "Bocadillo": (3.0, 300),
    "Ensalada": (2.5, 150)
}

print("Menú:")
for item, (precio, calorias) in menu.items():
    print(f"- {item}: {precio}€ ({calorias} cal)")


while True:
    producto = input("Ingresa el nombre del producto que deseas agregar (o 'fin' para terminar): ")
    if producto == "fin":
        break
    elif producto in menu:
        pedido.append(producto)
        precio, calorias = menu[producto]
        total_pagar += precio
        calorias_totales += calorias



print("Tu pedido: ")
for item in pedido:
    print(f"- {item}")

print(f"Total a pagar: {total_pagar:.2f}€")
print(f"Calorías totales: {calorias_totales} cal")
"""

def restapro(n1,n2):
    resta = n1-n2
    print(f"La resta de {n1} y de {n2} es: {resta}")
    
def dividepro(n1,n2):
    divide = n1/n2
    print(f"La division de {n1} y de {n2} es: {divide}")
    
def multipro(n1,n2):
    multi = n1-n2
    print(f"La multiplicacion de {n1} y de {n2} es: {multi}")
    
def sumapro2(n1,n2):
    suma = n1 + n2
    return suma
    
