#!/usr/bin/env python
#
# Método de Runge Kutta
#
# Ricardo Castro
# Oct/30/2023
# rcastro.AT.ite.dot.edu.dot.mx
#

def rk4(f, x0, y0, x1, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(y)
        k2 = h * f(y + 0.5 * k1)
        k3 = h * f(y + 0.5 * k2)
        k4 = h * f(y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vx, vy
