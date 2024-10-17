"""Ejercicio 1
1.Crea un programa llamado Funciones.py con las siguientes funciones:
Una función llamada mcd que reciba dos enteros a y b como parámetros y devuelva el máximo común divisor de esos 
parámetros. El máximo común divisor es el número más alto por el que se pueden dividir los dos números."""

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print(f"El máximo común divisor de {num1} y {num2} es {mcd(num1, num2)}")


"""2.Una función llamada esPrimo que reciba un número como parámetro y devuelva un booleano indicando
si el número es primo o no """ #Solo se dividen por ellos y el número 1 
def esPrimo(n):
    if n <= 1:# si es menor o igual que 1, no es primo
        return False #Si es primo 
    
    for i in range(n): 
        i += 1 #que parta en 1, no 0

        if i != 1 and i != n: #Siempre se dividirá por 1 o el mismo
            if n % i == 0: #Si el número es divisible por algún número entre 1 y el número mismo
                return False
    return True #Si no se encuentra ningún número que divide al número
            
primo = int(input("Introduce un número: "))
print(f"{primo} es primo: {esPrimo(int(primo))}")
         

"""Desde el programa principal, llama a la función mcd para 
calcular el máximo común divisor de 20 y 12 (debería dar 4),
 y usa la función esPrimo para sacar los números primos que haya del 1 al 50."""

#Función para calcular los primos del 1 al 50

for i in range(1, 51):
    if esPrimo(i):
        print(i, end=" ")


