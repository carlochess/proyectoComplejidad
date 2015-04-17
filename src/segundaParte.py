from lpSolv import *
from lector import *

def generarRestriccionesTipo(matriz, tipo):
    if tipo == 0 or tipo == 1:
        for j in range(0, n):
            restriccionCanecaI = []
            for k in range(0, i * n):
                if k >= i * j and k < i * j + i:
                    objPos = k % i
                    if tipo == 0:
                        restriccionCanecaI.append(items[objPos].getPeso())
                    elif tipo == 1:
                        restriccionCanecaI.append(items[objPos].getVolumen())
                else:
                    restriccionCanecaI.append(0)
            if tipo == 0:
                for k in range(0, 2*n):
                    if j == k:
                        restriccionCanecaI.append(-caneca.getPeso())
                    else:
                        restriccionCanecaI.append(0)
                restriccionCanecaI.append("<=")
                restriccionCanecaI.append(0)
            elif tipo == 1:
                for k in range(0, 2*n):
                    if j == k:
                        restriccionCanecaI.append(-caneca.getVolumen())
                    else:
                        restriccionCanecaI.append(0)
                restriccionCanecaI.append("<=")
                restriccionCanecaI.append(0)
            matriz.append(restriccionCanecaI)
    elif tipo == 2:
        for j in range(0, i):
            restriccionCanecaI = []
            for k in range(0, i * n+n):
                if (k % i) -j == 0 and k < i*n:
                    restriccionCanecaI.append(1)
                else:
                    restriccionCanecaI.append(0)
            restriccionCanecaI.append("=")
            restriccionCanecaI.append(1)
            matriz.append(restriccionCanecaI)
    elif tipo == 3:
        for j in range(0, n):
            restriccionCanecaI = []
            for k in range(0, i * n):
                if k >= i * j and k < i * j + i and k < i*n:
                    restriccionCanecaI.append(items[k% i].getPeso()*(n-1))
                else:
                    restriccionCanecaI.append(-items[k% i].getPeso())
            for k in range(0, n):
                restriccionCanecaI.append(0)
            for k in range(0, n):
                if k == j:
                    restriccionCanecaI.append(1)
                else:
                    restriccionCanecaI.append(0)
            restriccionCanecaI.append("=")
            restriccionCanecaI.append(1)
            matriz.append(restriccionCanecaI)
            # Para -a - I
            restriccionCanecaJ = []
            for k in range(0, i * n):
                if k >= i * j and k < i * j + i and k < i*n:
                    restriccionCanecaJ.append(-items[k% i].getPeso()*(n-1))
                else:
                    restriccionCanecaJ.append(items[k% i].getPeso())
            for k in range(0, n):
                restriccionCanecaJ.append(0)
            for k in range(0, n):
                if k == j:
                    restriccionCanecaJ.append(1)
                else:
                    restriccionCanecaJ.append(0)
            restriccionCanecaJ.append("=")
            restriccionCanecaJ.append(1)
            matriz.append(restriccionCanecaJ)
            

def generarFuncObj(matriz):
    restriccionCanecaI = []
    for k in range(0, i * n+n):
        restriccionCanecaI.append(0)
    for k in range(0, n):
        restriccionCanecaI.append(1)
    matriz.append(restriccionCanecaI)

def generarRestricciones():
    generarRestriccionesTipo(primeraRestriccion, 1)
    generarRestriccionesTipo(segundaRestriccion, 0)
    generarRestriccionesTipo(terceraRestriccion, 2)
    generarRestriccionesTipo(cuartaRestriccion, 3)

def generarFuncionObjetivo():
    generarFuncObj(funcObj)

def printMatrix(testMatrix):
    for i in range(len(testMatrix)):
        for j in range(len(testMatrix[i])):
            print(testMatrix[i][j], end=" ")
        print()
    print()
'''
def printMatrix(testMatrix):
    for i in range(len(testMatrix)):
        for j in range(len(testMatrix[i])):
            print testMatrix[i][j],
        print
    print
'''

o = leerArchivo()
caneca = o[0]
items=  o[1]
n = len(items)#int(hallarN())
i = len(items)
funcObj = []
primeraRestriccion = []
segundaRestriccion = []
terceraRestriccion = []
cuartaRestriccion = []
matriz = []
generarRestricciones()
generarFuncionObjetivo()
for e in funcObj:
    matriz.append(e)
for e in primeraRestriccion:
    matriz.append(e)
for e in segundaRestriccion:
    matriz.append(e)
for e in terceraRestriccion:
    matriz.append(e)
for e in cuartaRestriccion:
    matriz.append(e)
print("nObjetos: ", i , ", nCanecas=", n)
print(items)
printMatrix(matriz)
resolverParte2(matriz,n,i)
