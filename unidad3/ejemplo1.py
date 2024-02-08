import numpy as np
N = 10000
valores = np.random.rand(N)
suma_0 = 0
suma_1 = 0
p = 1 / 10
for valor in valores:
    if valor <= 1-p:
        suma_0 += 1
    else:
        suma_1 += 1

fracaso = round((suma_0/N)*100,2)
exito = round((suma_1/N)*100,2)
print(f'La probabilidad de fracasar es {fracaso}%, y que gane es {exito}%')
