ingresos = 0
gastos = 0

for n in range(3):
    ing = int(input("Dime tus tres ingresos"))
    ingresos = ingresos + ing
    n+=1
    
for n in range(3):
    gast = int(input("Dime tus tres gastos"))
    gastos = gastos + gast
    n+=1

total = ingresos - gastos
if total > 0:
    print("Balance positivos")
elif total == 0:
    print("Balance neutro")
elif total < 0:
    print("Balance negativo")