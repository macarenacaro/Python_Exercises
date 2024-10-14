"""Ejercicio 1

Crea un programa llamado Tuplas.py donde le pidas al usuario que rellene su dirección postal, 
que estará formada por su nombre de calle (texto), número de puerta (entero) y número de piso (entero). 
Almacena los datos en una tupla y luego muestra por pantalla el resultado (campo a campo)."""

calle = input("Introduce el nombre de la calle: ")
puerta = int(input("Introduce el número de la puerta: "))
piso = int(input("Introduce el número de piso: "))

tupla = (calle, puerta, piso)
for i in range(len(tupla)):
    print(f"Campo {i+1}: {tupla[i]}")



"""Ejercicio 2

Crea un programa llamado DiccionarioTuplas.py donde le pidas al usuario que rellene direcciones de 4 usuarios, 
identificados por su clave que será el DNI. Así, para cada usuario rellenará dicho DNI, y luego los datos de 
la dirección como en el ejercicio anterior (nombre de calle, número de puerta y número de piso). Almacenará los
 datos en un diccionario (asociando cada DNI con su dirección) y luego le pedirá al usuario que escriba un DNI 
 y mostrará los datos de su dirección, o el mensaje "El DNI no se encuentra almacenado" si no existe dicha clave."""


diccionarioTupla = {} #crear un diccionario vacío

for i in range(4): #Crear 4 usuarios
    dni = input(f"Introduce el DNI del usuario {i+1}: ") 
    calle = input(f"Introduce el nombre de la calle del usuario {i+1}: ")
    puerta = int(input(f"Introduce el número de la puerta del usuario {i+1}: "))
    piso = int(input(f"Introduce el número de piso del usuario {i+1}: "))

    tupla = (calle, puerta, piso) # crear una tupla con los datos de la dirección del usuario
    diccionarioTupla[dni] = tupla #clave : tupla


dni_busqueda = input("Introduce el DNI a buscar: ")#Solicitar al usuario que introduzca un DNI

for key,value in diccionarioTupla.items():#Recorrer el diccionario por key y value
    if key == dni_busqueda:
        print(f"Dirección del usuario con DNI {dni_busqueda}: {diccionarioTupla[dni_busqueda]}")
    else:
        print("El DNI no se encuentra almacenado")