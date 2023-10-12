#!/usr/bin/env python
#
# Primer ejemplo de generador de número aleatorio
#
# Ricardo Castro
# Aug/25/2023
# rcastro.AT.ite.DOT.edu.DOT.mx
# Se definen los valores iniciales
a = 16148
b = 5678
semilla = 367894
modulo = 99776654
# Se inicializa el arreglo
x = [semilla]
# Se agrega el valor al arreglo
# Se lleva a cabo la iteración
for i in range(1, 5):
    valor = (a * x[i-1] + b) % modulo
    x.append(valor)
x.pop(0)
for y in range(len(x)):
    x[y] = x[y]/modulo
for j in x:
    print(j)
