import utilidades as u

try:
    #1.Solicitar fichero sin "txt"
    fichero = input("Introduce el nombre del fichero, sin .txt: ") #Pedir fichero al usuario

    #2.Cargar los equipos del fichero a una lista 
    equipos = u.cargar_equipos(fichero) 

    #3.Ordenar y Clasificar los equipos, obteniendo el mejor equipo 
    mejorEquipo= u.clasificacion(equipos)

    #4. Obtener la tupla de la mejor y la peor racha del mejor equipo 
    tuplaRachas = u.racha(fichero,mejorEquipo)

    #5. Mostrar la mejor y la peor racha del mejor equipo
    print(f"Mejor y Peor Racha de {mejorEquipo}: {tuplaRachas}")

    #6.Que equipos les han goleado por almenos 4 o mas goles
    goleadores = u.goleadas(fichero) #Llamar a la función de goleadas
    print(f"Los equipos que han sido goleados por al menos 4 o más goles son: {goleadores}")

except:
    print("Fichero no encontrado")
    exit()
