'''
Actividad relacionada con la lección 4:

2. Haga uso de la función filter para construir un programa que, dado
una lista de n números devuelva aquellos que son primos. Por
ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente
debe devolver como resultado [3, 5, 5, 13]
'''
def primo(numero):
    cont = 0
    for i in range(1, numero):
        if numero % i == 0:
            cont += 1
            if cont > 1:
                return False
    return True

lista = [3, 4, 8, 5, 5, 22, 13]
solucion = list(filter(primo, lista))
print("Los números primos de la lista dada son:", solucion)