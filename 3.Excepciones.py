"""Crea un programa llamado Impares.py que pida al usuario un número entero positivo y muestre por pantalla todos los
números impares desde 1 hasta ese número, separados por comas. Si el número introducido no es un valor numérico entero,
o no es positivo, se lo deberá volver a pedir las veces que sean necesarias antes de hacer el conteo,
mostrando el mensaje de error correspondiente (por ejemplo, Número no válido)."""
   


correcto = False
while not correcto:
    try:
        n1 = int(input("Ingresa: "))


        if n1 <= 0:
            raise Exception()
       
        list = ""
        for i in range(n1):
         if i % 2 != 0:
            list = str(i)
        correcto = True


    except:
         print("Advertencia: el valor ingresado no es un número válido. Intenta de nuevo...")
