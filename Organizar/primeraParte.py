from __future__ import print_function
from Item import Item
from Mochila import Mochila
from lpSolv import *
from lector import *
import math
import sys

def generarRestriccionesTipo(matriz, tipo):
    if tipo == 0 or tipo == 1:
        restriccionCanecaI = []
        for k in range(0, i * n):
            objPos = k % i
            if tipo == 0:
                restriccionCanecaI.append(items[objPos].getPeso())
            elif tipo == 1:
                restriccionCanecaI.append(items[objPos].getVolumen())
        if tipo == 0:
            restriccionCanecaI.append(-caneca.getPeso())
        elif tipo == 1:
            restriccionCanecaI.append(-caneca.getVolumen())
        restriccionCanecaI.append("<=")
        restriccionCanecaI.append(0)
        matriz.append(restriccionCanecaI)
    else:
        for j in range(0, i):
            restriccionCanecaI = []
            for k in range(0, i * n):
                if (k % i) -j == 0 and k < i*n:
                    restriccionCanecaI.append(1)
                else:
                    restriccionCanecaI.append(0)
            restriccionCanecaI.append(0)
            restriccionCanecaI.append("=")
            restriccionCanecaI.append(1)
            matriz.append(restriccionCanecaI)

def generarFuncObj(matriz):
    restriccionCanecaI = []
    for k in range(0, i * n):
        restriccionCanecaI.append(0)
    restriccionCanecaI.append(1)
    matriz.append(restriccionCanecaI)


def hallarN():
    sumaPesos = 0
    sumaVolumenes = 0
    for i in range(len(items)):
        sumaPesos += items[i].getPeso()
    for i in range(len(items)):
        sumaVolumenes += items[i].getVolumen()
    pesos = math.ceil(sumaPesos / float(caneca.getPeso()))
    volumenes = math.ceil(sumaVolumenes / float(caneca.getVolumen()))
    if(pesos >= volumenes):
        return pesos
    else:
        return volumenes

def generarRestricciones():
    generarRestriccionesTipo(primeraRestriccion, 1)
    generarRestriccionesTipo(segundaRestriccion, 0)
    generarRestriccionesTipo(terceraRestriccion, 2)

def generarFuncionObjetivo():
    generarFuncObj(funcObj)

def printMatrix(testMatrix):
    for i in range(len(testMatrix)):
        for j in range(len(testMatrix[i])):
            print(testMatrix[i][j], end=" ")
        print(" : ", len(testMatrix[i]))
    print()


#items = [Item(20, 10), Item(20, 10), Item(20, 10), Item(20, 10),Item(20, 10)]
#caneca = Mochila(40, 10)
param = (sys.argv[1] if len(sys.argv) > 1 else -1)
o = leerArchivo(param)
caneca = o[0]
items=  o[1]
numeroProblema = o[2]+"_1.lp"
print("items: ",items)
print("mochila: ",caneca)
n = len(items)#int(hallarN())
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
print("nObjetos: ", i , ", nCanecas=", n)
printMatrix(matriz)
resolver(matriz,n,i,numeroProblema)
