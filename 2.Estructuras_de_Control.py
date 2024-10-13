"""Ejercicio 1: Crea un programa llamado Notas.py que le pida al usuario 3 notas, y calcule la nota final según estas reglas:
Si ninguna nota es mayor que 4, la nota final es 0
Si algunas notas son mayores que 4 (pero no todas), la nota final es 2
Si todas las notas son mayores que 4, la nota final será el 30% de la primera
más el 20% de la segunda más el 50% de la tercera"""
#MI RESPUESTA

contadorMayor = 0
rango = 3
list=[]

for i in range(rango):
    nota = int(input(f"Introduce la {i+1}º nota: "))
    list.append(nota)
    if nota > 4:
        contadorMayor =+1

if contadorMayor == 0:
    notafinal = 0
elif contadorMayor < 4 and contadorMayor > 0:
    notafinal= 2
elif contadorMayor == range:
    a= list[0] * 0.3
    b = list[1]*0.2
    c=list[3]*0.5

    notafinal = a+b+c
print(f" la nota final: {notafinal})


#PROFESOR RESPUESTA:
print("Escribe 3 notas: ")
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

if nota1 <=4 and nota2 <=4 and nota3 <=4:
    finalNote = 0
elif nota1 > 4 and nota2 > 4 and nota3 >4:
    finalNote = 0.3*nota1 + 0.2 * nota2 + 0.5 * nota3
else:
    finalNote = 2
print(f" la nota final: {finalNote}")
print("\n\n")



"""Ejercicio 2: Crea un programa llamado Factura.py que le pida al usuario precios para una factura, 
hasta que escriba 0. Entonces, el programa debe mostrar el total de la factura con 2 dígitos decimales."""

valor = 1.0
suma=0.0

while valor != 0:
    valor= float(input("Introduce números:"))
    suma = suma + valor

print(f"la suma es:{suma:.2f}")
print("\n\n")


"""Ejercicio 3:
Crea un programa llamado MayorMenor.py que le pida al usuario que introduzca una secuencia de N números positivos
(primero el usuario deberá indicar cuántos números va a introducir). Al final del proceso, el programa deberá mostrar
 por pantalla el valor del número mayor y el menor introducidos por el usuario. Por ejemplo:"""

intentos = int(input("Introduce nº intentos: "))
list=[]
for i in range(intentos):
    numero = int(input("Introduce numero: "))
    list.append(numero)

largest_number = max(list)
min_number = min(list)

print(f"El mas grande:{largest_number} \nel menor:{min_number}")
print("\n\n")


"""Ejercicio 4:
Crea un programa llamado MCD.py que le pida al usuario dos números n1 y n2 y utilice el algoritmo de Euclides para 
calcular su máximo común divisor (MCD). Este número es el divisor mayor que tienen en común los dos números. 
Aplicando el algoritmo de Euclides, se calcula de la siguiente forma:

Dividir el mayor de n1 y n2 entre el menor
Si la división es exacta (resto 0), el MCD es el número menor
Si no, se sustituye el número mayor por el resto de la división, y se vuelve al paso 1
Por ejemplo, para 20 y 12 haríamos algo así:

Dividimos 20 / 12. No es exacta, y el resto es 8. Reemplazamos 20 por 8
Dividimos 12 / 8. No es exacta, y el resto es 4. Reemplazamos 12 por 4
Dividimos 8 / 4. Es exacta, con lo que el MCD es 4."""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
resto = 1

while resto != 0:
    if numero1 > numero2:
        resto = numero1 % numero2
        print(f"Dividimos {numero1} / {numero2} y el resto {resto}")
        if resto == 0:
          mcd = numero2
          print(f"El MCD de {numero1} y {numero2} es {mcd}")
        else:
            numero1 = resto
    else: 
         numero1 , numero2 = numero2, numero1 #Intercambiamos los valores para seguir el algoritmo      

         