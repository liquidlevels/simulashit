#!/usr/bin/env python
#
# Generar tarjetas de débito
#
# Ricardo Castro
# Sep/22/2023
# rcastro.AT.ite.dot.edu.dot.mx
#
import sys
from datetime import date
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("270x395")
        self.title("Tarjeta de crédito")
        # Inicializa la información
        self.appat = tk.StringVar()
        self.apmat = tk.StringVar()
        self.nombre = tk.StringVar()
        self.vigencia = tk.StringVar()
        self.cvv = tk.StringVar()
        self.tarjeta = tk.StringVar()
        # Crear widgets
        self.crear_widgets()

    def crear_widgets(self):
        datos = Frame(self, relief=SUNKEN)
        datos.pack(fill=tk.X)
        #
        # Captura de información
        #
        ttk.Label(datos, text="Nombre", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        nombre = Entry(datos, textvariable=self.nombre)
        nombre.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Primer apellido", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        appat = Entry(datos, textvariable=self.appat)
        appat.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Segundo apellido", justify=LEFT, background="#C1E1C1").pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        apmat = Entry(datos, textvariable=self.apmat)
        apmat.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        #
        # Termina captura de información
        #
        # #############################
        # Creación de botones
        #
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TButton', background="blue", foreground="yellow")
        style.map('TButton', background=[('active', 'red')])
        ttk.Button(datos, text="Crear tarjeta", command=lambda: self.simular()).pack(side=tk.LEFT, padx=10, pady=5)
        ttk.Button(datos, text="Salir", command=lambda: self.quit()).pack(side=tk.LEFT, padx=10, pady=5)
        #
        # Aquí se visualizará la información
        #
        resultados = Frame(self, relief=SUNKEN)
        resultados.pack(fill=tk.X)
        ttk.Label(resultados, text="Fecha de vigencia", background='#1888d4', justify=LEFT).pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        vigencia = Entry(resultados, textvariable=self.vigencia)
        vigencia.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(resultados, text="CVV", background='#1888d4', justify=LEFT).pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        cvv = Entry(resultados, textvariable=self.cvv)
        cvv.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(resultados, text="Tarjeta de crédito", background='#1888d4', justify=LEFT).pack(
            anchor=tk.W, padx=10, pady=5, fill=tk.X
        )
        tarjeta = Entry(resultados, textvariable=self.tarjeta)
        tarjeta.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

    def contabiliza(self):
        suma = 0
        vocales = ('A', 'Á', 'À', 'E', 'É', 'È', 'I', 'Í', 'Ì', 'O', 'Ó', 'Ò', 'U', 'Ú', 'Ù')
        nombre_persona = self.nombre.get() + self.appat.get() + self.apmat.get()
        for caracter in nombre_persona:
            if caracter in vocales:
                suma += ord(caracter)
        return suma

    @staticmethod
    def mes_vigencia():
        mes_aleatorio = random.randint(1, 12)
        return mes_aleatorio

    @staticmethod
    def datos_tarjeta(semilla):
        parametro_t = 164976
        bandera = 1
        modulo = 2 ** 31
        valor_a = 8 * parametro_t + bandera * 3
        x = [semilla]
        for i in range(1, 10):
            temp = (valor_a * x[i - 1]) % modulo
            x.append(temp)
        for j in range(len(x)):
            # Convertir a str
            dato = str(x[j])
            # Se extraen los cuatro primeros caracteres
            x[j] = dato[:4]
        return x

    def simular(self):
        if not self.nombre.get():
            messagebox.showerror("Error", "No indicó el nombre")
            sys.exit(2)
        else:
            texto = self.nombre.get().upper()
            self.nombre.set(texto)
        if not self.appat.get():
            texto = "X"
            self.appat.set(texto)
        else:
            texto = self.appat.get().upper()
            self.appat.set(texto)
        if not self.apmat.get():
            messagebox.showerror("Error", "No indicó el apellido materno")
            sys.exit(2)
        else:
            texto = self.apmat.get().upper()
            self.apmat.set(texto)
        suma_vocales = self.contabiliza()
        mes_vigencia = self.mes_vigencia()
        # Fecha de vigencia
        hoy = date.today()
        anio_vigencia = hoy.year + 3
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
                'Diciembre']
        fecha_vigencia = meses[mes_vigencia-1] + '/' + str(anio_vigencia)
        # Para cálculo del CVV
        suma_total = suma_vocales + anio_vigencia + mes_vigencia
        cv1 = str(suma_total)
        cv = cv1[-3:]
        # Obtener los datos para la tarjeta
        semilla = int(cv)
        valores_tarjeta = self.datos_tarjeta(semilla)
        # Se conforma a la tarjeta
        digito2 = int(cv1[0])
        digito3 = int(cv1[1])
        digito4 = int(cv1[2])
        # Campos para la tarjeta
        campo1 = '5' + cv1[:3]
        campo2 = valores_tarjeta[digito2] if len(valores_tarjeta[digito2]) == 4 else '0' + valores_tarjeta[digito2]
        campo3 = valores_tarjeta[digito3] if len(valores_tarjeta[digito3]) == 4 else '0' + valores_tarjeta[digito3]
        campo4 = valores_tarjeta[digito4] if len(valores_tarjeta[digito4]) == 4 else '0' + valores_tarjeta[digito4]
        tarjeta = campo1 + '-' + campo2 + '-' + campo3 + '-' + campo4
        # Mostrar soluciones
        self.vigencia.set(fecha_vigencia)
        self.cvv.set(cv)
        self.tarjeta.set(tarjeta)

if __name__ == '__main__':
    app = App()
    app.mainloop()
