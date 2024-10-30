import auxiliar as aux

#1.Importar fichero
fichero = "delitos.txt"

#2. Lista de Delitos
listaDelitos = aux.crearListaDelitos(fichero) 

#3. Calcular  mes con más y menos delitos
listaMeses= aux.delitosPorMes(listaDelitos)

#4.Encontrar de la lista el número máximo y mínimo de delitos
max_delitos = max(listaMeses) 
min_delitos = min(listaMeses)

#5. Encontrar TODOS los meses que tienen el número máximo Y MINIMO de delitos
meses_con_mas_delitos = [i + 1 for i, x in enumerate(listaMeses) if x == max_delitos] #lista con todos los meses
meses_con_menos_delitos = [i + 1 for i, x in enumerate(listaMeses) if x == min_delitos] #lista con todos los meses

#6.Imprimir resultados
print(f"\nMes(es) con más delitos: {meses_con_mas_delitos}")
print(f"Mes(es) con menos delitos: {meses_con_menos_delitos}") #resultados 0

#7. Delitos de la localidad de Valladolid.
delitosLocalidad =aux.delitosPorLocalidad(listaDelitos, "Valladolid")

#8. Mostrar los resultados
print("\nDELITOS EN VALLADOLID:")
for delito in delitosLocalidad:
    print(delito.id, delito.mes, delito.localidad, delito.tipo)

#9. Mostrar nombre de las 3 localidades con más delitos.
top_localidades = aux.localidadesMasConflictivas(listaDelitos)
print("\nLas 3 localidades más conflictivas son:", top_localidades)
print()