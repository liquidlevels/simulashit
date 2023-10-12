#!/usr/bin/env python
#
# Cálculo de utilidad
#
# Ricardo Castro
# Sep/08/2023
# rcastro.AT.ite.dot.edu.dot.mx
#

import sys
import argparse
import csv
import numpy as np


class Verificar(object):
    def __init__(self, dias, anios, decimales, **kwargs):
        self.dias = dias
        self.anios = anios
        self.decimales = decimales
        for key, value in kwargs.items():
            if key == 'precio':
                if value <= 0:
                    print("No puede tener un precio negativo")
                    sys.exit(2)
                self.precio = value
            if key == 'demanda':
                self.venta_minima = value[0]
                self.venta_maxima = value[1]
                if self.venta_minima >= self.venta_maxima:
                    print("Existe un error con la demanda de venta estimada. Verifique")
                    sys.exit(2)
                if self.venta_minima <= 0 or self.venta_maxima <= 0:
                    print("Existe un error con la demanda de venta estimada. Verifique")
                    sys.exit(2)
            if key == 'costo_variable':
                self.costo_a = value[0]
                self.costo_c = value[1]
                self.costo_b = value[2]
                if self.costo_a <= 0 or self.costo_b <= 0 or self.costo_c <= 0:
                    print("Existe un error en la declaración de los costos")
                    sys.exit(2)
                if not self.costo_a < self.costo_c < self.costo_b:
                    print("Existe un error en la información de los costos. Verifique")
                    sys.exit(2)
            if key == 'costo_fijo':
                if value <= 0:
                    print("No se puede manejar un costo fijo negativo")
                    sys.exit(2)
                self.costo_fijo = value
            if key == 'j':
                if value <= 0:
                    print("Imposible realizar la simulación en la cantidad de días marcado")
                    sys.exit(2)
                self.dias = value
            if key == 'i':
                if value <= 0:
                    print("Imposible realizar la simulación por los años indicados")
                    sys.exit(2)
                self.anios = value
            if key == 'd':
                if value < 0:
                    print("No es posible redondear a la cantidad de decimales solicitados")
                    sys.exit(2)
                self.decimales = value


class Utilidad(Verificar):
    """ Métodos para el cálculo de la utilidad
        init.- Inicializar a la clase y esta a su vez a la clase padre
        demanda.- Crear la demanda estimada por los días y años indicados
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def crear_archivo(self, ingreso, costo, utilidad):
        data = []
        header = ['Año', 'Ingreso', 'Costo', 'Utilidad']
        for i in range(len(ingreso)):
            data.append([
                i + 1,
                round(ingreso[i], self.decimales),
                round(costo[i], self.decimales),
                round(utilidad[i], self.decimales)
            ])
        with open('utilidad.csv', 'w', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print('El archivo con la información ha sido creado')

    def demanda(self):
        demanda_estimada = np.random.randint(
            self.venta_minima,
            self.venta_maxima,
            [self.anios, self.dias]
        )
        return demanda_estimada

    def ingreso(self):
        demanda_estimada = self.demanda()
        demanda_promedio = np.mean(demanda_estimada, 1)
        ingreso_promedio = self.precio * demanda_promedio
        return ingreso_promedio

    def costo(self):
        demanda_estimada = self.demanda()
        costos_estimados = np.random.triangular(
            self.costo_a, self.costo_c, self.costo_b,
            [self.anios, self.dias]
        )
        costos_produccion = demanda_estimada * costos_estimados
        costos_promedios = self.costo_fijo + np.mean(costos_produccion, 1)
        return costos_promedios

    def simular(self):
        ingreso = self.ingreso()
        costo = self.costo()
        utilidad = ingreso - costo
        self.crear_archivo(ingreso, costo, utilidad)


def main(**kwargs):
    # Número de días a emplear
    dias = 365
    # Años por simular
    anios = 5
    # Decimales por emplear
    decimales = 2
    simular = Utilidad(dias, anios, decimales, **kwargs)
    simular.simular()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='simulacion6',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
            Cálculo de la utilidad, empleando una distribución uniforme para el ingreso,
            y una distribución distribución triangular para el costo.
            Suponga que la demanda del producto es de 500 a 1000 piezas.
            Para ejecutar el código, debe declararse como
                            <archivo.py> --demanda 500 1000
            Es decir, debe declarar en la línea, la información correspondiente
            al intervalo de la demanda de la producción.
            Este mismo formato aplica para ingresar los costos variables. Suponga
            que los costos de producción son a = 16, c = 20 y b = 24; entonces,
                        <archivo.py> --demanda 500 1000 --costos 16 20 24
            ''',
    epilog='''
            La información se mandará a un archivo llamado utilidad.csv
            '''
)
    parser.add_argument('-p', '--precio', dest="precio",
                        help='Precio del artículo', type=float,
                        required=True)
    parser.add_argument('-v', '--demanda', dest="demanda",
                        help='Intervalo de producción o venta estimada', type=int,
                        required=True, nargs=2)
    parser.add_argument('-c', '--costos', dest="costo_variable",
                        help="Costo variable en distribución triangular", type=float,
                        required=True, nargs=3)
    parser.add_argument('-C', '--cfijo', dest="costo_fijo",
                        help="Costo Fijo", type=float,
                        required=True)
    parser.add_argument('-d', '--dias', default=365, dest='j',
                        help='Días que dura la simulación (default: %(default)s)',
                        type=int, nargs='?', required=False)
    parser.add_argument('-y', '--anio', default=5, dest='i',
                        help='Días que dura la simulación (default: %(default)s)',
                        type=int, nargs='?', required=False)
    parser.add_argument('-D', '--decimales', default=2, dest='d',
                        help='Número de decimales por redondear (default: %(default)s)',
                        type=int, nargs='?', required=False)
    datos_ingreso = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}
    main(**datos_ingreso)
