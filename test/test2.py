from scipy import integrate
import numpy as np

# Definir la función de densidad de probabilidad
def exp_density(x):
    return (1/4) * np.exp(-1/4 * x)

# Calcular la probabilidad utilizando la integral
probability, error = integrate.quad(exp_density, 4, 5)

# Imprimir el resultado
print("La probabilidad es:", probability)
