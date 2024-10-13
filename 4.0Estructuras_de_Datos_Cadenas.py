#   SOSSSSSS
"""Ejecicio 1: Crea un programa llamado SumaSecuencia.py que le pida al usuario una secuencia de números separados por
espacios y calcule la suma total de esos números."""

# Solicitar al usuario una secuencia de números separados por espacios
numeros = input("Introduce una secuencia de números separados por espacios: ")

# Convertir la cadena de números en una lista de enteros
numeros_lista = [int(numero) for numero in numeros.split()]

# Calcular la suma de los números
suma_total = sum(numeros_lista)

# Mostrar el resultado
print(f"La suma total de los números es: {suma_total}")
print("\n\n")


"""Ejercicio 2: Crea un programa llamado CuentaTexto.py que le pida al usuario un texto, y luego le diga 
cuántas veces aparece la palabra Python en ese texto."""
cuenta = input("Introduce un cuento: ")
contador= 0
lista = cuenta.split()#transformamos la cadena en una lista

for palabra in lista:
    print(palabra)
    if palabra.lower() == "python":
        contador += 1
        
print(f"Aparece un total de {contador}")
print("\n\n")