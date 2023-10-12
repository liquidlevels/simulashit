#!/usr/bin/env python
#-*-coding: utf-8 -*-
#
# Generador de contraseñas seguras
#
# Ricardo Castro
# Mar/23/22
# rcastro.at.ite.dot.edu.dot.mx
#

import sys,random

def realizar_contrasenia(cuantos):
    may=["A","B","C","D","E","F","G","K","N","P","Q","W","V","Z","Y"]
    minu=["a","f","h","i","j","l","n","s","r","t","y","u","b"]
    num=["0","1","2","3","4","5","6","7","8","9"]
    sig=["*","#","$","!","?","&","%"]
    contra=''
    for i in range(cuantos):
        opcion=random.randint(1,4)
        if opcion==1:
            valor=may[random.randint(0,len(may)-1)]
            contra=contra+valor
        elif opcion==2:
            valor=minu[random.randint(0,len(minu)-1)]
            contra=contra+valor
        elif opcion==3:
            valor=num[random.randint(0,len(num)-1)]
            contra=contra+valor
        elif opcion==4:
            valor=sig[random.randint(0,len(sig)-1)]
            contra=contra+valor
    return(contra)

def valorar(num_caracteres):
    if num_caracteres<=0:
        print('Intente con otro valor')
        sys.exit(2)
    else:
        contrasenia=realizar_contrasenia(num_caracteres)
        print(contrasenia)

def main():
    while True:
        try:
            n=int(input("Número de caracteres para la contraseña: "))
            break
        except:
            print("Por favor, indique otro valor ")
    valorar(n)

if __name__ == '__main__':
    main()
