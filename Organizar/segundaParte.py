from __future__ import print_function
from lector import *
from lpSolv import *
import sys

def generarRestriccionesTipo(matriz, tipo):
    numeroRestricciones = (n* (n-1)) / 2
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
                for k in range(0, numeroRestricciones+n):
                    if j == k:
                        restriccionCanecaI.append(-caneca.getPeso())
                    else:
                        restriccionCanecaI.append(0)
                restriccionCanecaI.append("<=")
                restriccionCanecaI.append(0)
            elif tipo == 1:
                for k in range(0, numeroRestricciones+n):
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
            for k in range(0, i * n + numeroRestricciones+n):
                if (k % i) -j == 0 and k < i * n:
                    restriccionCanecaI.append(1)
                else:
                    restriccionCanecaI.append(0)
            restriccionCanecaI.append("=")
            restriccionCanecaI.append(1)
            matriz.append(restriccionCanecaI)
    elif tipo == 3:
        r = 0
        for u in range(0, n):
            for v in range(u + 1, n):
                mult = 1
                for numEq in range(0, 2):
                    restriccionCanecaI = []
                    for k in range(0, i * n):
                        if k >= u * i and k < u * i + i:
                            restriccionCanecaI.append(mult * items[k % i].getPeso())
                        elif k >= v * i and k < v * i + i:
                            restriccionCanecaI.append(-mult * items[k % i].getPeso())
                        else:
                            restriccionCanecaI.append(0)
                    for k in range(0, n):
                        restriccionCanecaI.append(0)
                    for k in range(0, numeroRestricciones):
                        if k == r:
                            restriccionCanecaI.append(-1)
                        else:
                            restriccionCanecaI.append(0)
                    restriccionCanecaI.append("<=")
                    restriccionCanecaI.append(0)
                    matriz.append(restriccionCanecaI)
                    mult = mult * -1
            	r += 1

def generarFuncObj(matriz):
    restriccionCanecaI = []
    numeroRestricciones = (n* (n-1)) / 2
    for k in range(0, i * n +n):
        restriccionCanecaI.append(0)
    for k in range(0, numeroRestricciones):
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
        print(" : ",len(testMatrix[i]))
    print()

param = (sys.argv[1] if len(sys.argv) > 1 else -1)
o = leerArchivo(param)
caneca = o[0]
items = o[1]
numeroProblema = o[2] + "_2.lp"
n = 2#len(items)#int(hallarN())
i = len(items)
funcObj = []
primeraRestriccion = []
segundaRestriccion = []
terceraRestriccion = []
cuartaRestriccion = []
matriz = []
numeroRestricciones=(n* (n-1)) / 2
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
print("Items ", items)
print("Caneca ", caneca)
printMatrix(matriz)
resolverParte2(matriz,n,i,numeroProblema,numeroRestricciones)

