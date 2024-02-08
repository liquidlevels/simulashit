def suma_unicode(cadena):
    suma = 0
    for caracter in cadena:
        suma += ord(caracter)
        print(ord(caracter))
    return suma

# Ejemplo de uso
cadena_ejemplo = "Hola"
resultado = suma_unicode(cadena_ejemplo)
print("La suma de los valores Unicode es:", resultado)
