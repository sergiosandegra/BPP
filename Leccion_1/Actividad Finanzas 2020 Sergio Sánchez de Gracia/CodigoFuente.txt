from csv import reader
from collections import Counter
from matplotlib import pyplot as plt

try:
    with open('finanzas2020.csv', 'r') as archivo:
        print("Archivo abierto correctamente")
        lineas = reader(archivo, delimiter = '\t')
        lista = list(lineas)
        mesesDelAnio = lista[0]
        lista.pop(0)
        array=[]
        array2=[]
        cont = 0

        if len(mesesDelAnio)==12:
            print("El archivo contiene 12 meses")
            while(cont <= 11):
                for lis in lista:
                    l=list(map(int,lis))
                    array2.append(l[cont])

                array.append(array2)
                array2=[]
                cont += 1

        else:
            print("Falta algún mes")


except FileNotFoundError as e:
        print("No se encuentra el archivo")
        exit()


def gastos(array,mesesDelAnio):
    meses = []
    gastos=[]
    cont=0

    for i in array:
        for j in i:
            if j<0:
                gastos.append(j*(-1))
        meses.append(sum(gastos))
        gastos=[]

    gastosPorMes=dict(zip(mesesDelAnio,meses))
    return gastosPorMes

#print(gastos(array,mesesDelAnio))

def ingresos(array, mesesDelAnio):
    meses = []
    ingresos=[]

    for i in array:
        for j in i:
            if j>0:
                ingresos.append(j)
        meses.append(sum(ingresos))
        ingresos=[]

    ingresosPorMes=dict(zip(mesesDelAnio,meses))
    return ingresosPorMes

#print(ingresos(array,mesesDelAnio))

def ahorros(array,mesesDelAnio):
    g=gastos(array,mesesDelAnio)
    i=ingresos(array,mesesDelAnio)
    ahorrosPorMes=dict(Counter(i)-Counter(g))

    return ahorrosPorMes

#print(ahorros(array,mesesDelAnio))


# EJERCICIO 1: ¿Qué mes se ha gastado más?
def mesMasGastos(array,mesesDelAnio):
    meses = gastos(array,mesesDelAnio)
    dinero=meses.values()
    maxDinero=max(int(num) for num in dinero)
    for key, value in meses.items():
         if maxDinero == value:
             mes= key

    return (mes,maxDinero)

#print("Mes con más gastos", mesMasGastos(array,mesesDelAnio))


# EJERCICIO 2: ¿Qué mes se ha ahorrado más?
def mesMasAhorros(array,mesesDelAnio):
    meses = ahorros(array,mesesDelAnio)
    dinero=meses.values()
    maxDinero=max(int(num) for num in dinero)
    for key, value in meses.items():
         if maxDinero == value:
             mes= key
    return (mes,maxDinero)

#print("Mes con más ahorros ", mesMasAhorros(array,mesesDelAnio))

# EJERCICIO 4: ¿Cuál ha sido el gasto total a lo largo del año?
def GastoTotalAnio(array,mesesDelAnio):
    g=gastos(array,mesesDelAnio)
    dinero=g.values()
    totalGastos = sum(dinero)
    return totalGastos

#print("Gasto total al año ", GastoTotalAnio(array,mesesDelAnio))

# EJERCICIO 3: ¿Cuál es la media de gastos al año?
def mediaGastosAnio(array,mesesDelAnio):
    totalGastos=GastoTotalAnio(array,mesesDelAnio)
    media = totalGastos/12
    return media

#print("Media de gastos al año ", mediaGastosAnio(array,mesesDelAnio))

# EJERCICIO 5: ¿Cuáles han sido los ingresos totales a lo largo del año?
def IngresoTotalAnio(array,mesesDelAnio):
    i=ingresos(array,mesesDelAnio)
    dinero=i.values()
    totalIngresos = sum(dinero)

    return totalIngresos

#print("Total ingresos al año ", IngresoTotalAnio(array,mesesDelAnio))

# EJERCICIO 6: Opcional: Realice una gráfica de la evolución de ingresos a lo largo del año .
def dibuja(mesesDelAnio,array):
    ingresosPorMes=ingresos(array, mesesDelAnio)
    array1=mesesDelAnio
    array2=ingresosPorMes.values()

    plt.plot(array1, array2, marker='o')
    plt.xlabel('Año (meses)')
    plt.ylabel('Ingresos ($)')
    plt.title('Evolución de ingresos a lo largo del año')
    plt.show()
dibuja(mesesDelAnio,array)
