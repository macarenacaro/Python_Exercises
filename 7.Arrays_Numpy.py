"""Crea un programa en Python llamado ArrayCeros.py que defina un array unidimensional de 10 ceros (enteros) en NumPy. 
Después, cambia el tercer cero por un 1. Imprime el resultado final."""

"""import numpy as np

# Definimos un array unidimensional de 10 ceros
array_ceros = np.zeros(10, dtype=int)

# Cambiamos el tercer cero por un 1
array_ceros[2] = 1

# Imprimimos el resultado final
print(array_ceros)
"""


"""Crea un programa llamado NumerosNoNulos.py que le pida al usuario una secuencia de números separada por espacios, y 
cree con ella un array unidimensional de NumPy. Después, deberá quedarse con los números que no sean ceros, y mostrar
el array resultado por pantalla. Deberá también indicar el valor mayor y menor introducido por el usuario (sin contar 
los ceros previamente filtrados)."""

import numpy as np

# Solicitar al usuario una secuencia de números separados por espacios
numeros = input("Introduce una secuencia de números separados por espacios: ")

# Convertir una lista de enteros
numeros_lista = list(map(int, numeros.split()))

# Crear un array unidimensional de NumPy con los números introducidos
array_numeros = np.array(numeros_lista)
print(array_numeros)

# Filtrar los números que no sean ceros
array_noceros = array_numeros[array_numeros!= 0]
print(array_noceros)

# Calcular el valor mayor y menor
mayor = array_noceros.max()
print(mayor)

# Calcular el valor mayor y menor
mayor = array_noceros.min()
print(mayor)