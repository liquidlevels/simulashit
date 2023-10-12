#!/usr/bin/env python
#
# Clase generadora de números aleatorios
#
# Ricardo Castro
# Aug/25/2023
# rcastro.AT.ite.dot.edu.dot.mx
#
import sys
import argparse

class Aleatorios(object):
    def __init__(self, parametro_a, parametro_b, modulo, semilla, cantidad, decimales, **kwargs):
        self.parametro_a = parametro_a
        self.parametro_b = parametro_b
        self.modulo = modulo
        self.semilla = semilla
        self.cantidad = cantidad
        self.decimales = decimales
        for key, value in kwargs.items():
            if key in 'a':
                if value <= 0:
                    print('El parámetro a no puede ser negativo')
                    sys.exit(2)
                self.parametro_a = value
            if key in 'b':
                if value <= 0:
                    print('El parámetro b no puede ser negativo')
                    sys.exit(2)
                self.parametro_b = value
            if key in 'm':
                if value <= 0:
                    print('El módulo no puede ser negativo')
                    sys.exit(2)
                self.modulo = value
            if key in 's':
                if value <= 0:
                    print('La semilla no puede ser negativa')
                    sys.exit(2)
                self.semilla = value
            if key in 'n':
                if value <= 0:
                    print('La cantidad de aleatorios solicitada no es posible de generar')
                    sys.exit(2)
                self.cantidad = value
            if key in 'd':
                if value <= 0:
                    print('El parámetro d no puede ser negativo')
                    sys.exit(2)
                self.decimales = value
            if self.modulo <= self.parametro_a or self.modulo <= self.parametro_b or self.modulo <= self.semilla:
                print("El módulo debe ser la mayor cantidad de los parámetros a emplear")
                sys.exit(2)

class Generar(Aleatorios):
    """Clase que contendrá al método para generar los números aleatorios"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def aleatorios(self):
        # Se inicializa el arreglo
        x = [self.semilla]
        # Se lleva a cabo la iteración
        for i in range(1, self.cantidad + 1):
            valor = (self.parametro_a * x[i - 1] + self.parametro_b) % self.modulo
            x.append(valor)
        x.pop(0)
        for y in range(len(x)):
            x[y] = round(x[y] / self.modulo, self.decimales)
        return x

def main(parametro_a=16598, parametro_b=11642, modulo=99778465, semilla=94786, cantidad=5, decimales=2, **kwargs):
    iniciar = Generar(parametro_a, parametro_b, modulo, semilla, cantidad, decimales, **kwargs)
    aleatorios = iniciar.aleatorios()
    for aleatorio in aleatorios:
        print(aleatorio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='simulacion3',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
        Clase para generar valores aleatorios empleando el método congruencial
        x_(n+1) = (ax_n+b) mod (m)
        Donde:
        a Valor multiplicativo
        b Término independiente
        m Módulo
        A partir de la semilla X0, el sistema empleará este algoritmo para generar una
        n cantidad de valores, que posteriormente serán divididos entre el valor m, generando
        así un arreglo de valores entre 0 y 1
        ''',
        epilog='''
        En caso de no declarar ningún valor, el sistema ya cuenta con valores declarados por
        omisión (default)
        '''
    )
    parser.add_argument('-a', '--terminoA', default=16598, dest="a",
                        help='Valor multiplicativo (default: %(default)s)', type=int,
                        nargs='?', required=False)
    parser.add_argument('-b', '--terminoB', default=11642, dest='b',
                        help='Término independiente (default: %(default)s)', type=int,
                        nargs='?', required=False)
    parser.add_argument('-m', '--modulo', default=99778465, dest='m',
                        help='Módulo(default: %(default)s)', type=int,
                        nargs='?', required=False)
    parser.add_argument('-s', '--semilla', default=94786, dest='s',
                        help='Valor inicial o semilla del generador (default: %(default)s)',
                        type=int, nargs='?', required=False)
    parser.add_argument('-n', '--cantidad', default=5, dest='n',
                        help='Cantidad de valores aleatorios por generar (default: %(default)s)',
                        type=int, nargs='?', required=False)
    parser.add_argument('-d', '--decimales', default=2, dest='d',
                        help='Número de decimales por redondear (default: %(default)s)',
                        type=int, nargs='?', required=False)
    args = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}
    main(**args
