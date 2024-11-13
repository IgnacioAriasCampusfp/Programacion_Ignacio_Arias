import numpy as np

Valor =  np.random.randint(1, 51, size=(4, 3))
print(Valor)

maximo = np.max(Valor, axis=0)

print(maximo)