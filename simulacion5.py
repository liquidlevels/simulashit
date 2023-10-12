#!/usr/bin/env python
#
# Método para generar valores aleatorios en un intervalo [a,b]
#
# Ricardo Castro
# Sep/06/2023
# rcastro.AT.ite.dot.edu.dot.mx
#

import sys
import argparse
import csv
from datetime import datetime


class Aleatorios(object):
    def __init__(self, cantidad, decimales, parametro_t, bandera, modulo, **kwargs):
        self.cantidad = cantidad
        self.decimales = decimales
        self.parametro_t = parametro_t
        self.bandera = bandera
        self.modulo = modulo
        for key, value in kwargs.items():
            if key == 'intervalo':
                self.valor_inicial = value[0]
                self.valor_final = value[1]
            if key == 'n':
                if value <= 0:
                    print('No es posible generar la cantidad de aleatorios solicitados')
                    sys.exit(2)
                self.cantidad = value
            if key == 'd':
                if value < 0:
                    print('No es posible redondear a la cantidad solicitada')
                    sys.exit(2)
                self.decimales = value
            if key == 't':
                if value <= 0:
                    print('El parámetro t es incorrecto')
                    sys.exit(2)
                self.parametro_t = value
            if key == 'flag':
                self.bandera = value
        if self.valor_inicial >= self.valor_final:
            print('No es posible realizar los valores aleatorios en el intervalo')
            sys.exit(2)


class Generar(Aleatorios):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def aleatorios(self):
        parametro_a = 8 * self.parametro_t + (self.bandera * 3)
        ahora = datetime.now()
        semilla = ahora.microsecond
        x = [semilla]
        for i in range(1, self.cantidad + 1):
            valor = (parametro_a * x[i-1]) % self.modulo
            x.append(valor)
        x.pop(0)
        aleatorios = [aleatorio / self.modulo for aleatorio in x]
        return aleatorios


    def crear_archivo(self, valores):
        data = [] # Arreglo donde estará la información que se manda a archivo
        header = ['Num', 'Valores'] # Encabezado del archivo de salida
        for i in range(len(valores)):
            data.append([i + 1, valores[i]])
        with open('salida.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print('El archivo ha sido generado')


    def simular(self):
        constante = self.valor_final-self.valor_inicial
        aleatorios = self.aleatorios()
        valores = [round(constante * rnd + self.valor_inicial, self.decimales) for rnd in aleatorios]
        self.crear_archivo(valores)


def main(**kwargs):
    # Cantidad de aleatorios a ser generados
    cantidad = 6
    # Cantidad de decimales a emplear para el redondeo
    decimales = 2
    # Valor del parámetro <t> para obtener <a>
    parametro_t = 159
    # Bandera (1 si es suma, -1 si es resta)
    bandera = 1
    # Valor del módulo a emplear
    modulo = 2 ** 31
    # Se envían los datos a la clase generadora de valores aleatorios
    iniciar = Generar(cantidad, decimales, parametro_t, bandera, modulo, **kwargs)
    iniciar.simular()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    prog='simulacion5',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
        Generador de valores aleatorios en un intervalo [a,b] empleando el
        método congruencial multiplicativo.
        Suponga por ejemplo, que desea construir valores en el intervalo [5.35,14.16]; donde
        los valores deben ser a 2 decimales y requiere 6 aleatorios.
        Un ejemplo de la instrucción será:
                    <archivo.py> -i 5.35 14.16 -n 6 -d 2
        Es decir, debe declarar al intervalo con el valor inicial, un espacio, y posteriormente un
        valor final.
        ''',
    epilog='''
        El usuario podrá determinar la cantidad de aleatorios a ser generados así como la
        cantidad de decimales por emplear; sin embargo, el valor del módulo no es modificable
        y se asigna como 2 ** 31.
        La información será enviada hacia un archivo denominado 'salida.csv' en la misma ruta
        en la que se encuentre éste archivo
        '''
    )
    parser.add_argument('-i', '--intervalo', dest="intervalo",
                        help='Intervalo para generar valor aleatorio.',
                        type=float, nargs=2, required=True)
    parser.add_argument('-n', '--cantidad', default=6, dest='n',
                        help='Cantidad de valores aleatorios por generar (default: %(default)s)',
                        type=int, nargs='?', required=False)
    parser.add_argument('-d', '--decimales', default=2, dest='d',
                        help='Número de decimales por redondear (default: %(default)s)',
                        type=int, nargs='?', required=False)
    parser.add_argument('-t', '--terminoT', default=159, dest="t",
                        help='Valor multiplicativo para obtener el valor a (default: %(default)s)', type=int,
                        nargs='?', required=False)
    parser.add_argument('-B', '--bandera', default=1, dest='flag', choices=[1, -1],
                        help='Define si es suma (1) o resta (-1) (default: %(default)s)', type=int,
                        nargs='?', required=False)
    datos_ingreso = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}
    main(**datos_ingreso)
