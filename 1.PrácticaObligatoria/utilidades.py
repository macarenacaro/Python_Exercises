import equipo as e

def goleadas(fichero):

    listaGoleadas = [] 

    with open(f"{fichero}.txt", "r") as f: #abrir el fichero
        lineas = f.readlines()
        
        for linea in lineas:
            # Reemplazar "#" por "," y dividir la línea en componentes
            linea = linea.replace("#", ",").strip().split(",")
            
            # Asignar cada dato a una variable
            equipo1, gol1, equipo2, gol2 = linea[0], int(linea[1]), linea[2], int(linea[3])

            if gol1 - gol2 >= 4:  # Si equipo2 perdió por goleada
                listaGoleadas.append(equipo2)
            elif gol2 - gol1 >= 4:  # Si equipo1 perdió por goleada
                 listaGoleadas.append(equipo1)
        
    listaGoleadas = list(set(listaGoleadas)) # eliminar duplicados set es un Conjunto
    return listaGoleadas




    return 

def cargar_equipos(fichero):
    lista = [] #creo una lista vacía para almacenar los objetos equipo
    with open(f"{fichero}.txt", "r") as f: #abrir el fichero leer el contenido
        lineas = f.readlines()
        for linea in lineas:
            # Reemplazar "#" por "," y dividir la línea en componentes
            linea = linea.replace("#", ",").strip().split(",")
            
            # Asignar cada dato a una variable 
            equipo1, gol1, equipo2, gol2 = linea[0], int(linea[1]), linea[2], int(linea[3])
            
            # Llamar a evaluacionPartido
            eq1, eq2 = evaluacionPartido(equipo1, gol1, equipo2, gol2)

            # Desempaquetar cada equipo y crear objeto Equipo
            objetoEquipo1 = e.Equipo(eq1[0], eq1[1], eq1[2], eq1[3], eq1[4], eq1[5])
            objetoEquipo2 = e.Equipo(eq2[0], eq2[1], eq2[2], eq2[3], eq2[4], eq2[5])
            
            # Añadir objetos a la lista
            guardar_equipo(objetoEquipo1, lista)
            guardar_equipo(objetoEquipo2, lista)

    return lista

def clasificacion(equipos): #recibe la lista de equipos y los ordena
    equipos.sort(key=lambda x: (-x.pt, -x.goles_favor, x.goles_contra, x.nombre))  
    #-x.pt ordena primero por puntos en orden descendente. (mayor a menor)
        #-x.goles_favor: prioriza los equipos con más goles a favor en caso de empate en puntos
            #x.goles_contra: da prioridad a los equipos con menos goles en contra (menos a mas)
                #x.nombre asegura un orden alfabético 

    print("\nCLASIFICACION FINAL")
    print(f"{' ':<15} {'G':>5} {'E':>5} {'P':>5} {'F':>4} {'C':>5} {'Pt':>5}")
  
    for equipo in equipos:
        equipo.mostrar()

    print("\nGanador de la liga: ",(equipos[0].nombre).upper())
    return equipos[0].nombre

def racha(fichero, nombre_equipo):

    # Variables para las rachas actuales y máximas de victorias y derrotas
    racha_victorias_actual = 0
    racha_derrotas_actual = 0
    rachasVictorias = []
    rachasDerrotas = []
    
   
    with open(f"{fichero}.txt", "r") as f: #abrir el fichero
        lineas = f.readlines()
        
        for linea in lineas:
            # Reemplazar "#" por "," y dividir la línea en componentes
            linea = linea.replace("#", ",").strip().split(",")
            
            # Asignar cada dato a una variable
            equipo1, gol1, equipo2, gol2 = linea[0], int(linea[1]), linea[2], int(linea[3])
            
            # Revisar si el equipo es el mismo
            if equipo1 == nombre_equipo or equipo2 == nombre_equipo: #si está en el equipo1 o el equipo2
                if equipo2 == nombre_equipo: # Si el nombre_equipo es el equipo2
                    equipo1, gol1, equipo2, gol2 = equipo2, gol2, equipo1, gol1  # Intercambio los equipos y goles
                    #Esto lo hacemos para evaluar siempre nuestro equipo como el equipo1.

                if gol1 > gol2:  # Victoria
                    racha_victorias_actual += 1
                    rachasDerrotas.append(racha_derrotas_actual)
                    racha_derrotas_actual = 0 #Racha de derrotas reseteada

                elif gol1 < gol2: # Pierde
                    racha_derrotas_actual += 1
                    rachasVictorias.append(racha_victorias_actual)
                    racha_victorias_actual = 0 #Racha de victorias reseteada

                else:  # Empate
                    rachasVictorias.append(racha_victorias_actual)#añado ultimo valor de mi racha de victorias
                    rachasDerrotas.append(racha_derrotas_actual)#añado ultimo valor de mi racha de derrotas
                    racha_victorias_actual = 0 #resetear rachas actuales
                    racha_derrotas_actual = 0

    # Incluir las últimas rachas del bucle
    rachasVictorias.append(racha_victorias_actual)
    rachasDerrotas.append(racha_derrotas_actual)

    # Retornar como tupla con victorias y la peor racha de derrotas
    tuplaRachas = (max(rachasVictorias), max(rachasDerrotas))
    return tuplaRachas

def evaluacionPartido(equipo1,gol1,equipo2,gol2):
    if gol1 > gol2: #Ver partidos Ganados
        ganados1= 1
        ganados2= 0
        empate1 = 0
        empate2 = 0
        perdido1 = 0
        perdido2= 1

    elif gol1 < gol2:
        ganados1= 0
        ganados2 = 1
        empate1 = 0
        empate2 = 0
        perdido1 = 1
        perdido2= 0
    else: 
        ganados1= 0
        ganados2 = 0
        empate1 = 1
        empate2 = 1
        perdido1 = 0
        perdido2= 0

    return (equipo1,ganados1,empate1,perdido1,gol1,gol2),(equipo2,ganados2,empate2,perdido2,gol2,gol1)


# Método para Guardar todos los equipos en una Lista
def guardar_equipo(self,lista):       
    for equipo in lista:
        if equipo.nombre == self.nombre:#si se está repitiendo el equipo, se actualizan sus datos
            # print(f"El equipo {self.nombre} ya existe. Actualizando datos")
            equipo.ganado = equipo.ganado + self.ganado
            equipo.empatado = equipo.empatado + self.empatado
            equipo.perdido = equipo.perdido + self.perdido
            equipo.goles_favor = equipo.goles_favor+ self.goles_favor
            equipo.goles_contra = equipo.goles_contra + self.goles_contra
            equipo.pt = (equipo.ganado*3) + 1*equipo.empatado  # Puntos totales
            return
    lista.append(self) # sino añadimos el equipo a la lista
    return