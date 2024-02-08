#!/usr/bin/python3
# -*-coding: utf-8 -*-
#
# Ejemplo de valores discretizados
#
# Ricardo C.
# Abr/27/23
# rcastro.at.ite.dot.edu.dot.mx
#
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    intervalo_1 = 0
    intervalo_2 = 0
    intervalo_3 = 0
    intervalo_4 = 0
    intervalo_5 = 0
    intervalo_6 = 0
    intervalo_7 = 0
    n = 100000
    aleatorios = np.round(np.random.rand(n), 4)
    for valor in aleatorios:
        if valor <= 0.0062:
            intervalo_1 += 1
        elif 0.0062 < valor <= 0.0668:
            intervalo_2 += 1
        elif 0.0668 < valor <= 0.3081:
            intervalo_3 += 1
        elif 0.3081 < valor <= 0.691:
            intervalo_4 += 1
        elif 0.691 < valor <= 0.9309:
            intervalo_5 += 1
        elif 0.9309 < valor <= 0.9908:
            intervalo_6 += 1
        else:
            intervalo_7 += 1
    valores = np.array([intervalo_1, intervalo_2, intervalo_3, intervalo_4, intervalo_5, intervalo_6, intervalo_7])
    valores = np.around(valores/sum(valores) * 100, 2)
    X = ('19.85', '23.03', '26.21', '29.39', '32.57', '35.75', '38.93')
    fig, ax = plt.subplots()
    rects1 = ax.bar(X, valores, 0.4, color='maroon')
    for index, data in enumerate(valores):
        ax.text(x=index, y=data+0.5, s=f"{data}%", fontdict=dict(fontsize=8), ha='center')
    ax.set_xlabel('Escala')
    ax.set_ylabel('Probabilidad')
    plt.show()
