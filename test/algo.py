import numpy as np
from scipy.stats import norm

# Media y desviación estándar deseadas
media_deseada = 10
desviacion_deseada = 2

# Valores aleatorios generados
valores_aleatorios = [0.043, 0.155, 0.109, 0.989, 0.591, 0.678, 0.968, 0.685, 0.376, 0.738, 0.933, 0.753, 7.018, 1.018]

# Transformación a la distribución normal deseada
valores_transformados = media_deseada + desviacion_deseada * np.sqrt(2) * norm.ppf(valores_aleatorios)

# Imprimir los resultados
for i, valor_transformado in enumerate(valores_transformados):
    print(f'X_{i+1} = {valor_transformado}')

