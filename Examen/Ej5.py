electricidaad = int(input("Cuantos has gastado en electricidad"))
agua = int(input("Cuantos has gastado en agua"))
gas = int(input("Cuantos has gastado en gas"))
comida = int(input("Cuantos has gastado en comida"))

total= electricidaad+ agua+ gas+comida

if total > 500:
    print("Has gastado mucho")
else:
    print("No has gastado")