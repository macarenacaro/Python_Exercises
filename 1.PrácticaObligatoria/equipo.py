class Equipo:

    # Constructor
    def __init__(self, nom, g,e,p, f,c):
        self.nombre = nom
        self.ganado = g
        self.empatado = e
        self.perdido = p
        self.goles_favor = f
        self.goles_contra = c
        self.pt = (g*3) + 1*e  # Puntos totales


    # Otro método de ejemplo
    def mostrar(self):
        print(f"{self.nombre:<15} {self.ganado:>5} {self.empatado:>5} {self.perdido:>5}"
              f"{self.goles_favor:>5} {self.goles_contra:>5} {self.pt:>5}")
        

    
