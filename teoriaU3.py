#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
import math
import random
from decimal import *
getcontext().prec=2


suma=0
n=50000

for i in range(0,n):
    t=-2.374*math.log(random.random())
    if(t>=6):
        suma+=1.0

probabilidad=(suma/n)*100
print('La probabilidad es de {0:.2f}%'.format(probabilidad))
