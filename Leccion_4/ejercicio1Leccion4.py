'''
Actividad relacionada con la lección 4:
1. Haciendo uso de comprensión de listas realice un programa que, dado
una lista de listas de números enteros, devuelva el máximo de cada
lista. Por ejemplo, suponga la siguiente listas de listas:
[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

El programa debe devolver el mayor elemento de cada sublista
(señalado en negrita).

Ahora, haciendo uso del pdb, inserte puntos de parada justo en la línea
donde ha implementado la compresión de listas. Haga pruebas
mostrando el contenido de las variables y continuar con la ejecución
línea a línea. ¿Qué conclusiones obtiene?
'''

numeros = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]

solucion = [max(i) for i in numeros]

print("El mayor elemento de cada sublista es:", solucion)