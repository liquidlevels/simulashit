#!/usr/bin/env python
#
# Ricardo Castro
# Sep/15/2023
# rcastro.AT.ite.dot.edu.dot.mx
#
import math
import argparse
import numpy as np


class Parametros(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'contra':
                self.contrasenia = value
                semilla = 0
                for caracter in value:
                    if caracter not in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'):
                        semilla += ord(caracter)
                self.semilla = semilla


class Encriptar(Parametros):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def cambiardigitos(digitos):
        decimales = [10, 11, 12, 13, 14, 15]
        hexadecimal = ['A', 'B', 'C', 'D', 'E', 'F']
        for c in range(7):
            if digitos == decimales[c-1]:
                digitos = hexadecimal[c-1]
        return digitos

    def decimalhexadecimal(self, decimal):
        hexadecimal = ''
        while decimal != 0:
            rem = self.cambiardigitos(decimal % 16)
            hexadecimal = str(rem) + hexadecimal
            decimal = int(decimal / 16)
        return hexadecimal

    def encriptar(self):
        # Se crea lo que será la nueva contraseña
        palabra = ''
        rng = np.random.default_rng(self.semilla)
        valores_aleatorios = rng.random(len(self.contrasenia))
        # Se multiplica cada número aleatorio por el valor ASCII correspondiente
        for i in range(len(self.contrasenia)):
            caracter_en_ascii = ord(self.contrasenia[i])
            termino = self.decimalhexadecimal(math.floor(caracter_en_ascii * valores_aleatorios[i]))
            palabra += termino
        return palabra

def main(**kwargs):
    # Se inicializa la clase para encriptar la contraseña
    iniciar = Encriptar(**kwargs)
    # Se manda llamar al método de la clase que realiza la encriptación
    nueva_contrasenia = iniciar.encriptar()
    print(nueva_contrasenia)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog ='simula8',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
        Programa que encripta una contraseña.
        """,
        epilog="""
        Se muestra en pantalla el término encriptado correspondiente.
        """
    )
    parser.add_argument('-p', '--palabra',
                        help="Contraseña a ser encriptada", required=True, type=str,
                        dest="contra")
    datos_ingreso = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}
    main(**datos_ingreso)
