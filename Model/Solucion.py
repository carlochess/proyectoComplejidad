# -*- coding: utf-8 -*-
from __future__ import print_function
from .Mochila import Mochila
class Solucion:
    def __init__(self,mochila, items, matriz):
        self.numMochilas = 0
        print(mochila)
        self.mochila = mochila
        self.items = items
        self.MatrizSolucion = matriz

    def getMochila(self):
        return self.mochila

    def procesarSegundaSolucion(self, variables,numMochilas,numObjetos, numProblema,varAbs):
        self.mochilas = []
        for i in range(numMochilas):
            self.mochilas.append(Mochila(self.mochila.getVolumen(), self.mochila.getPeso()))
        for i in range(numMochilas * numObjetos):
            if variables[i] != 0:
                item = self.items[i % numObjetos]
                mochilaTemp = self.mochilas[int(i / numObjetos)]
                item.setMochila(int(i / numObjetos))
                mochilaTemp.addVolumen(item.getVolumen())
                mochilaTemp.addPeso(item.getPeso())
        self.nombreArchivoSol = str(numProblema)
        self.vectorSolucion = variables
        self.numeroMochilas = numMochilas
        #print("nObjetos: ", self.i , ", nself.mochilas=", self.n)
        #self.printMatrix(self.matriz)

    def procesarPrimeraSolucion(self, variables,numMochilas,numObjetos, numProblema,varAbs, numeroMochilas):
        self.mochilas = []
        for i in range(numMochilas):
            self.mochilas.append(Mochila(self.mochila.getVolumen(), self.mochila.getPeso()))
        for i in range(numMochilas * numObjetos):
            if variables[i] != 0:
                item = self.items[i % numObjetos]
                mochilaTemp = self.mochilas[int(i / numObjetos)]
                item.setMochila(int(i / numObjetos))
                mochilaTemp.addVolumen(item.getVolumen())
                mochilaTemp.addPeso(item.getPeso())
        self.nombreArchivoSol = str(numProblema)
        self.vectorSolucion = variables
        self.numeroMochilas = numeroMochilas

    def getNumeroMochilas(self):
        return self.numeroMochilas

    def guardarSalida(variables, numMochilas, numObjetos, ejercicio):
        f = open("Salida/" + str(ejercicio), 'w')
        for i in range(numMochilas * numObjetos):
            if variables[i] != 0:
                f.write("El objeto " + str(i % numObjetos) + " ira en la maleta " + str(int(i / numObjetos)) + "\n")
        f.close()

    def getItem(self, i):
        return self.items[i]
    def getItems(self):
        return self.items

    def getVolumenesMaletas(self):
        arr = []
        for mochila in self.mochilas:
            arr.append(mochila.getVolumenContenido())
        return arr
    def getPesosMaletas(self):
        arr = []
        for mochila in self.mochilas:
            arr.append(mochila.getPesoContenido())
        return arr

    def printMatrix(self,testMatrix):
        for i in range(len(testMatrix)):
            for j in range(len(testMatrix[i])):
                print(testMatrix[i][j], end=" ")
            print()
        print()