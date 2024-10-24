"""Ejercicio 1
Escribe un programa en Python llamado Jugadores.py que defina una clase llamada Jugador, 
con atributos dorsal (numérico) y nombre (texto). Define el constructor para darles valor 
y un método que muestre la información de un jugador con el formato dorsal. Nombre.. 
Por ejemplo: 16. Pau Gasol​. En el programa principal, crea un par de jugadores con sus datos, 
y muestra su información por pantalla.​
"""
"""class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = int(dorsal)  # Convierte el dorsal a entero
        self.nombre = nombre

      # Metodo para mostrar el nombre del jugador
    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre}.")  


gamer1 = Jugador(18, "Macarena Caro")
gamer2 = Jugador(20, "Carla U")
gamer1.mostrar()
gamer2.mostrar()"""

"""Ejercicio 2
Escribe una nueva versión del ejercicio anterior en un programa llamado Equipos.py donde, 
además de la clase Jugador haya una segunda clase llamada Equipo, cuyo único atributo será el nombre 
del equipo (texto), junto con un constructor para darle valor​. Haz que cada jugador pueda pertenecer a un 
equipo añadiendo un atributo Equipo a la clase Jugador. En el programa principal, crea un jugador y un equipo,
y asigna el equipo al jugador. Muestra por pantalla la información del jugador, incluyendo el equipo."""

"""class Jugador:
    def __init__(self, d, n, e):
        self.dorsal = d  # Convierte el dorsal a entero
        self.nombre = n
        self.equipo = e  # Añade el equipo al jugador

      # Metodo para mostrar el nombre del jugador
    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre}, {self.equipo.nombre}")    

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre


team = Equipo("San Vicente")
gamer3 = Jugador(18, "Macarena Caro", team)

gamer3.mostrar()"""


"""Ejercicio 3
En un hospital hay diferentes tipos de personal: médicos, enfermeros y administrativos. De todos guardamos 
su información básica (dni, nombre, dirección y teléfono), de los médicos almacenamos también su especialidad, 
y de los enfermeros la planta en la que trabajan. ​
Al hospital acuden pacientes. De todos ellos se guarda un historial con su dni, nombre, dirección, teléfono, 
y un conjunto de pruebas y consultas que hayan hecho en el hospital. De cada prueba o consulta guardamos la 
fecha en que se hizo, y el médico que le atendió ​

Define las clases necesarias para el enunciado propuesto en un programa llamado Hospital.py. Define un programa 
principal que cree un array de personal de hospital con varios médicos y enfermeros. Define un paciente con sus datos,
 y dale de alta diversas pruebas realizadas por varios médicos. Finalmente, trata de mostrar por pantalla los datos 
 completos del paciente, incluyendo su historial de pruebas.​
"""