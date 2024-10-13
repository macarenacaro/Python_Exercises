"""Ejercicio 1
Crea un programa llamado ListaInvertida.py que le pida al usuario que introduzca un conjunto de nombres
separados por comas, y le muestre por pantalla la misma lista en orden inverso."""

nombres=input("Introduce nombres")
lista_nombres = nombres.split(',')
lista_nombres.reverse()
print(lista_nombres)

"""
Ejercicio 2: 
Crea un programa llamado BuscaNumeros.py que le pida al usuario que escriba números. 
El programa los irá añadiendo uno tras otro a una lista hasta que el usuario escriba 0. Entonces, 
le pedirá que diga un número y le indicará en qué posiciones de la lista aparece ese número.
"""

numeros = []
while True:
    numero = int(input("Introduce un número (0 para salir): "))
    if numero == 0:
        break
    numeros.append(numero)

numero_buscado = int(input("Introduce un número a buscar: "))

for i, num in enumerate(numeros): #enumerate devuelve una lista con los índices y los valores
    if num == numero_buscado:
        print(f"El número {numero_buscado} aparece en la posición {i}")


"""Ejercicio 3: 
Crea un programa llamado Identidad.py que le pida al usuario un tamaño de tabla N y luego le deje rellenar 
los datos de N filas y N columnas de enteros. Al finalizar, le deberá decir si la tabla que ha rellenado 
se corresponde o no con una matriz identidad. Una matriz identidad es aquella que tiene unos en su diagonal 
principal y ceros en el resto. Por ejemplo (para un tamaño 3 x 3):
1 0 0
0 1 0
0 0 1"""

n = int(input("Introduce el tamaño de la tabla: "))

tabla = [] # Crear una lista vacía para la tabla
for i in range(n):
    list = [] #crear una lista vacía para cada fila
    for j in range(n):
        valor = int(input(f"Dato en la posición ({i},{j}): ")) 
        list.append(valor)
        if j == n - 1: # si es la última columna de la fila, agregar la lista a la tabla
            tabla.append(list)             
    print()
#tabla = [[int(input(f"Dato en la posición ({i},{j}): ")) for j in range(n)] for i in range(n)], esto hace eso


for fila in tabla: # Accedemos a cada fila (que es una lista) (juan.maca)
    print(*fila)


contador = 0
valor_diagonal = 0
for i in range(n): #Vemos posicion
    for j in range(n):
        if i == j:# es decir [0][0],[1][1],[2][2]...
            if i == 0: #solo atribuirá valor la primera posición[0][0]
                valor_diagonal = tabla[i][j] #el resto debe tener este valor
            if valor_diagonal== tabla[i][j]:
                contador += 1

if contador == n:
    print("La tabla es una matriz identidad")
else:
    print("La tabla no es una matriz identidad")
