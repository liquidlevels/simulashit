#!/usr/bin/env python
#
# Problema de Población
#
# Ricardo Castro
# Nov/10/2023
# rcastro.AT.ite.dot.edu.dot.mx
#

import math
from scipy import stats
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from operaciones import rk4
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Población")
        self.geometry("300x500")
        # Inicializar la información
        self.tiempo_inicial = tk.IntVar() # Tiempo inicial
        self.tiempo_final = tk.IntVar() # Tiempo final
        self.pobl_infectada_inicial = tk.DoubleVar() # Personas originalmente infectadas
        self.pobl_infectada_final = tk.DoubleVar() # Personas infectadas posteriormente
        self.poblacion = tk.DoubleVar() # Personas que habitan en la zona
        # Crear los campos
        self.crear_widgets()
    
    def crear_widgets(self):
        # Se crea el Frame para solicitar la información
        datos = Frame(self, height=2, bd=1, relief=SUNKEN)
        datos.pack(fill=X, padx=5, pady=5)
        # Captura de información
        ttk.Label(datos, text="Tiempo inicial", justify=LEFT).pack(fill=BOTH, expand=True)
        tiempo_inicial = Entry(datos, width=16, textvariable=self.tiempo_inicial)
        tiempo_inicial.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Tiempo final", justify=LEFT).pack(fill=BOTH, expand=True)
        tiempo_final = Entry(datos, width=16, textvariable=self.tiempo_final)
        tiempo_final.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Personas infectadas inicialmente", justify=LEFT).pack(fill=BOTH, expand=True)
        personas_enfermas_inicio = Entry(datos, width=16,textvariable=self.pobl_infectada_inicial)
        personas_enfermas_inicio.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Personas infectadas posteriormente", justify=LEFT).pack(fill=BOTH, expand=True)
        personas_enfermas_final = Entry(datos, width=16, textvariable=self.pobl_infectada_final)
        personas_enfermas_final.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        ttk.Label(datos, text="Población", justify=LEFT).pack(fill=BOTH, expand=True)
        pob = Entry(datos, width=16, textvariable=self.poblacion)
        pob.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
        # Se crea el Frame para los botones
        botones = Frame(self, height=2, bd=1, relief=SUNKEN)
        botones.pack(fill=X, padx=5, pady=5)
        ttk.Button(botones, text="Graficar", command=lambda:self.resolver()).pack(side=tk.LEFT, padx=10, pady=5)
        ttk.Button(botones, text="Salir", command=self.quit).pack(side=tk.LEFT, padx=10, pady=5)

    def parametro_k(self):
        x0 = self.tiempo_inicial.get()
        y0 = math.log(self.pobl_infectada_inicial.get())
        x1 = self.tiempo_final.get()
        y1 = math.log(self.pobl_infectada_final.get())
        x = [x0, x1]
        y = [y0, y1]
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return slope

    def funcion(self, y):
        k = self.parametro_k()
        valor_a = self.poblacion.get()
        valor_b = valor_a / k
        return k * y * (valor_a - valor_b * y)

    def simular(self):
        vx, vy = rk4(self.funcion, self.tiempo_inicial.get(),
        self.pobl_infectada_inicial.get(), self.tiempo_final.get() + 4, 100)
        # Se crea una figura contenedora
        fig = Figure(figsize=(5, 5), dpi=100)
        # Se crea una sub figura dentro de la misma
        plot1 = fig.add_subplot(111)
        # Se crea la gráfica
        plot1.plot(vx, vy)
        # Se añade a Tkinter, elemento Canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack()

    def resolver(self):
        bandera = 0
        tiempo_inicio = self.tiempo_inicial.get()
        if tiempo_inicio < 0:
            messagebox.showerror("Error en el tiempo inicial", "El tiempo inicial no puede ser negativo")
        else:
            bandera += 1
        if not self.tiempo_final.get():
            messagebox.showerror("Error", "No se ha declarado el tiempo final")
        else:
            if self.tiempo_final.get() <= 0:
                messagebox.showerror("Error en el tiempo", "El tiempo final no puede ser negativo")
            else:
                bandera += 1
        if not self.pobl_infectada_inicial.get():
            messagebox.showerror("Error", "No seha declarado el número de personas infectas originalmente")
        else:
            if self.pobl_infectada_inicial.get() <= 0:
                messagebox.showerror("Error en población", "La población infectada originalmente no puede ser negativa")
            else:
                bandera += 1
        if not self.pobl_infectada_final.get():
            messagebox.showerror("Error", "No se ha declarado al número de personas infectadas posteriormente")
        else:
            if self.pobl_infectada_final.get() <= 0:
                messagebox.showerror("Error en población", "El número de personas infectadas posteriormente no puede ser negativa")
            else:
                bandera += 1
        if not self.poblacion.get():
            messagebox.showerror("Error", "No se ha declarado la población")
        else:
            if self.poblacion.get() <= 0:
                messagebox.showerror("Error en población", "La población no puede ser negativa")
            else:
                bandera += 1
        if bandera == 5:
            self.simular()
    
def main():
        app = App()
        app.mainloop()
    
if __name__ == '__main__':
        main() 
