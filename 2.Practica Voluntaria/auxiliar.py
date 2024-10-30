
import Delito as d
def crearListaDelitos(fichero):
    listaDelitos = []

    # Abrir el fichero y leer el contenidos
    with open(fichero, "r", encoding='utf-8') as f:
        lineas = f.readlines()
        for linea in lineas:
            # Dividir la línea en componentes
            linea = linea.strip().split(",")

            # Crear un objeto delito y añadirlo a la lista
            objetoDelito = d.Delito(linea[0], int(linea[1]), linea[2], linea[3])
            listaDelitos.append(objetoDelito)

    return listaDelitos

def delitosPorMes(lista):
    listDelitosMes = [0]*12 #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for delito in lista:
        listDelitosMes[delito.mes - 1] += 1 #sumamos uno al mes correspondiente
    return listDelitosMes

def delitosPorLocalidad(lista, localidad):
    listaDelitosLocalidad = []
    for delito in lista:
        if delito.localidad == localidad:
            listaDelitosLocalidad.append(delito)#añadimos objeto delito a la lista

    return listaDelitosLocalidad #devolvemos lista de delitos de la localidad especificada

def localidadesMasConflictivas(lista):

    contadorDelitos = {} #crearemos un diccionario vacío para contar los delitos por localidad
                        #localidad : Cantidad

    # Contar los delitos por localidad
    for delito in lista:
        if delito.localidad in contadorDelitos: #si existe
            contadorDelitos[delito.localidad] += 1 #sumamos uno
        
        else: #si no existe
            contadorDelitos[delito.localidad] = 1 #localidad : 1
        
        
    # Ordenar las localidades por la cantidad de delitos en orden descendente
    localidades_ordenadas = sorted(contadorDelitos.items(), key=lambda x: x[1], reverse=True)

    # Obtener las tres localidades con más delitos
    localidades_mas_conflictivas = [localidad for localidad, _ in localidades_ordenadas[:3]]

    # Ordenar las localidades alfabéticamente 
    localidades_mas_conflictivas.sort() 

    return localidades_mas_conflictivas
    