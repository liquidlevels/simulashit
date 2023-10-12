#!/usr/bin/env python
#
# Método congruencial multiplicativo para generar números aleatorios
#
# Ricardo Castro
# Sept/04/2023
# rcastro.AT.ite.dot.edu.dot.mx
#

import sys
import argparse
from datetime import datetime


class Aleatorios(object):
    def __init__(self, parametro_t, bandera, modulo, cantidad, decimales, **kwargs):
        self.parametro_t = parametro_t
        self.bandera = bandera
        self.modulo = modulo
        self.cantidad = cantidad
        self.decimales = decimales
        for key, value in kwargs.items():
            if key in 't':
                if value <= 0:
                    print('El parámetro t debe ser entero positivo')
                    sys.exit(2)
                self.parametro_t = value
            elif key in 'b':
                self.bandera = value
            elif key in 'n':
                if value <= 0:
                    print('No es posible generar una cantidad negativa de aleatorios')
                    sys.exit(2)
                self.cantidad = value
            elif key in 'd':
                if value <= 0:
                    print('No es posible redondear hacia una cantidad negativa de aleatorios')
                    sys.exit(2)
                self.decimales = value


class Generar(Aleatorios):
    """Métodos para generar los números aleatorios"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def aleatorios(self):
        parametro_a = 8 * self.parametro_t + (self.bandera * 3)
        ahora = datetime.now()
        semilla = ahora.microsecond
        x = [semilla]
        for i in range(1, self.cantidad + 1):
            valor = (parametro_a * x[i - 1]) % self.modulo
            x.append(valor)
        x.pop(0)
        aleatorios = [round(aleatorio / self.modulo, self.decimales) for aleatorio in x]
        return aleatorios


def main(**kwargs):
    # Valor del parámetro <t> del generador
    parametro_t = 5678
    # Valor del parámetro bandera (suma = 1, resta = -1)
    bandera = 1
    # Valor del módulo para el generador (no se permite modificar)
    modulo = 2 ** 31# Número de aleatorios por crear
    cantidad = 4
    # Decimales por redondear
    decimales = 2
    inicio = Generar(parametro_t, bandera, modulo, cantidad, decimales, **kwargs)
    aleatorios = inicio.aleatorios()
    for aleatorio in aleatorios:
        print(aleatorio)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    prog='simulacion4',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
    El programa realiza la generación de números pseudo - aleatorios empleando el método congruencial
    multiplicativo
                                    X_(n+1)=(a*x_n)mod(m).
    Donde:
        a=(8*t) +/- 3               el parámetro t debe ser un entero positivo y entero.
        x_n                         indica el valor anterior que es empleado para obtener
                                    al nuevo valor
        El primer valor (o dato inicial conocido como semilla) se obtendrá del
        reloj de la computadora.
    Así entonces, los valores pseudo - aleatorios son aquellos que posteriormente se obtengan al
    dividir cada dato entre el módulo (m).
    Por omisión, el código supondrá la suma para la obtención del valor a; pudiendo ser modificado
    como resta en caso de así requerirse, al indicar como dato de entrada el valor b = -1.
    ''',
    epilog='''
    El usuario podrá determinar la cantidad de valores pseudo - aleatorios por ser generados; sin
    embargo, el valor del módulo no es modificable y se asigna como 2**31.
    '''
    )
    parser.add_argument('-t', '--parametro', default=5678, dest="t",
                        help='Coeficiente t del generador (default: %(default)s)',
                        nargs='?', type=int, required=False)
    parser.add_argument('-b', '--bandera', default=1, dest="b",
                        help='Determina si se emplea la suma o resta (default: %(default)s)',
                        nargs='?', type=int, choices=[1, -1], required=False)
    parser.add_argument('-n', '--cantidad', default=4, dest="n",
                        help='Número de aleatorios por generar (default: %(default)s)',
                        nargs='?', type=int, required=False)
    parser.add_argument('-d', '--decimales', default=2, dest="d",
                        help='Redondeo de decimales (default: %(default)s)',
                        nargs='?', type=int, required=False)
    entrada = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}
    main(**entrada)
