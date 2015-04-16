from Item import Item
from Mochila import Mochila
from lpSolv import *
import math

def generarRestriccionesTipo(matriz, tipo):
    if tipo == 0 or tipo == 1:
        for j in range(0, n):
            restriccionCanecaI = []
            for k in range(0, i * n):
                if k >= i * j and k < i * j + i:
                    objPos = k % n
                    if tipo == 0:
                        restriccionCanecaI.append(items[objPos].getPeso())
                    elif tipo == 1:
                        restriccionCanecaI.append(items[objPos].getVolumen())
                else:
                    restriccionCanecaI.append(0)
            if tipo == 0:
                for k in range(0, n):
                    if j == k:
                        restriccionCanecaI.append(-caneca.getPeso())
                    else:
                        restriccionCanecaI.append(0)
                restriccionCanecaI.append("<=")
                restriccionCanecaI.append(0)
            elif tipo == 1:
                for k in range(0, n):
                    if j == k:
                        restriccionCanecaI.append(-caneca.getVolumen())
                    else:
                        restriccionCanecaI.append(0)
                restriccionCanecaI.append("<=")
                restriccionCanecaI.append(0)
            matriz.append(restriccionCanecaI)
    else:
        for j in range(0, i):
            restriccionCanecaI = []
            for k in range(0, i * n + 2):
                if k == j or k == j + 4:
                    restriccionCanecaI.append(1)
                else:
                    restriccionCanecaI.append(0)
            restriccionCanecaI.append("=")
            restriccionCanecaI.append(1)
            matriz.append(restriccionCanecaI)

def generarFuncObj(matriz):
    restriccionCanecaI = []
    for k in range(0, i * n):
        restriccionCanecaI.append(0)
    for k in range(0, n):
        restriccionCanecaI.append(1)
    matriz.append(restriccionCanecaI)


def hallarN():
    sumaPesos = 0
    sumaVolumenes = 0
    for i in range(len(items)):
        sumaPesos += items[i].getPeso()
    for i in range(len(items)):
        sumaVolumenes += items[i].getVolumen()
    if(sumaPesos >= sumaVolumenes):
        return math.ceil(sumaPesos / caneca.getPeso())
    else:
        return math.ceil(sumaVolumenes / caneca.getVolumen())

def generarRestricciones():
    generarRestriccionesTipo(primeraRestriccion, 0)
    generarRestriccionesTipo(segundaRestriccion, 1)
    generarRestriccionesTipo(terceraRestriccion, 2)

def generarFuncionObjetivo():
    generarFuncObj(funcObj)

def printMatrix(testMatrix):
    for i in range(len(testMatrix)):
        for j in range(len(testMatrix[i])):
            print(testMatrix[i][j], end=" ")
        print()
    print()


items = [Item(20, 10), Item(20, 10), Item(20, 10), Item(20, 10)]
caneca = Mochila(40, 10)
n = hallarN()
i = len(items)
funcObj = []
primeraRestriccion = []
segundaRestriccion = []
terceraRestriccion = []
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
printMatrix(matriz)
resolver(matriz)