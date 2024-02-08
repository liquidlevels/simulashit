#!/usr/bin/env python
# -*-coding: utf-8 -*-
#
# Ejemplo para distribuciones
#
# Ricardo C.
# Oct/28/22
# rcastro.at.ite.dot.edu.dot.mx
#
import numpy as np
from time import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    suma_0 = 0
    suma_500 = 0
    suma_1000 = 0
    suma_2000 = 0
    suma_5000 = 0
    n = 100000
    inicio = time()
    for i in range(n):
        x = round(np.random.rand(), 2)
        if x <= 0.60:
            suma_0 += 1
        elif 0.61 <= x <= 0.80:
            suma_500 += 1
        elif 0.81 <= x <= 0.90:
            suma_1000 += 1
        elif 0.91 <= x <= 0.95:
            suma_2000 += 1
        else:
            suma_5000 += 1
    final = time() - inicio
    valores = np.array([suma_0, suma_500, suma_1000, suma_2000, suma_5000]) 
    valores = np.around(valores/sum(valores) * 100, 2)
    print("Tiempo de ejecución: %0.10f segundos" % final)
    pagos = ('0', '500', '1000', '2000', '5000')
    plt.bar(pagos, valores, 0.4, color='maroon')
    plt.xlabel('Pagos a efectuar')
    plt.ylabel('Probabilidad de realizar el pago')
    plt.show()
