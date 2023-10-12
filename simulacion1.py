#!/usr/bin/env python
#
# Primer generador de aleatorios
#
# Ricardo Castro
# Aug/25/2023
# rcastro.AT.ite.dot.edu.dot.mx
#
a = 151516
b = 1918
semilla = 23456
modulo = 575629
# Se declara el arreglo
x = []
x.append(semilla)
# Comienza el ciclo
for i in range(1, 11):
    zeta = (a * x[i-1] + b) % modulo
    x.append(zeta)

for j in range(len(x)):
    x[j] = x[j]/modulo

for m in x:
    print('{:0.5f}'.format(m))
