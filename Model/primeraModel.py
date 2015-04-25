# -*- coding: utf-8 -*-
class PrimeraParteModel:

    def __init__(self,descriptionBoxes,volumeBackpack,maximumWeightBackpack):
        from .Item import Item
        from .Mochila import Mochila
        from .lpSolv import resolver

        self.items = []
        self.mochila = None
        for listaCaja in descriptionBoxes:
            self.items.append(Item(int(listaCaja[1]),int(listaCaja[2])))
        print(self.items)
        self.mochila=Mochila(volumeBackpack,maximumWeightBackpack)
        print(self.mochila)
        numeroProblema = self.nombreProblema+"_1.lp"
        self.n = len(self.items)#int(self.hallarN())
        self.i = len(self.items)
        funcObj = []
        self.primeraRestriccion = []
        self.segundaRestriccion = []
        self.terceraRestriccion = []
        self.matriz = []
        self.generarRestricciones()
        self.generarFuncObj(self.matriz)
        for e in funcObj:
            self.matriz.append(e)
        for e in self.primeraRestriccion:
            self.matriz.append(e)
        for e in self.segundaRestriccion:
            self.matriz.append(e)
        for e in self.terceraRestriccion:
            self.matriz.append(e)
        print("nObjetos: ", self.i , ", nself.mochilas=", self.n)
        self.printMatrix(self.matriz)
        self.optimumNumberPeople = resolver(self.matriz,self.n,self.i,numeroProblema)

    def setProblemName(self, nombre):
        self.nombreProblema = "0"
        print(self.nombreProblema)

    def generarRestriccionesTipo(self, matriz, tipo):
        i=self.i
        if tipo == 0 or tipo == 1:
            for j in range(0, self.n):
                restriccioncanecaI = []
                for k in range(0, i * self.n):
                    if k >= i * j and k < i * j + i:
                        objPos = k % i
                        if tipo == 0:
                            restriccioncanecaI.append(self.items[objPos].getPeso())
                        elif tipo == 1:
                            restriccioncanecaI.append(self.items[objPos].getVolumen())
                    else:
                        restriccioncanecaI.append(0)
                if tipo == 0:
                    for k in range(0, self.n):
                        if j == k:
                            restriccioncanecaI.append(-self.mochila.getPeso())
                        else:
                            restriccioncanecaI.append(0)
                    restriccioncanecaI.append("<=")
                    restriccioncanecaI.append(0)
                elif tipo == 1:
                    for k in range(0, self.n):
                        if j == k:
                            restriccioncanecaI.append(-self.mochila.getVolumen())
                        else:
                            restriccioncanecaI.append(0)
                    restriccioncanecaI.append("<=")
                    restriccioncanecaI.append(0)
                matriz.append(restriccioncanecaI)
        else:
            for j in range(0, i):
                restriccioncanecaI = []
                for k in range(0, i * self.n+self.n):
                    if (k % i) -j == 0 and k < i*self.n:
                        restriccioncanecaI.append(1)
                    else:
                        restriccioncanecaI.append(0)
                restriccioncanecaI.append("=")
                restriccioncanecaI.append(1)
                matriz.append(restriccioncanecaI)

    def generarFuncObj(self, matriz):
        restriccioncanecaI = []
        for k in range(0, self.i * self.n):
            restriccioncanecaI.append(0)
        for k in range(0, self.n):
            restriccioncanecaI.append(1)
        matriz.append(restriccioncanecaI)


    def hallarN(self):
        import math
        sumaPesos = 0
        sumaVolumenes = 0
        for i in range(len(self.items)):
            sumaPesos += self.items[i].getPeso()
        for i in range(len(self.items)):
            sumaVolumenes += self.items[i].getVolumen()
        pesos = math.ceil(sumaPesos / float(self.mochila.getPeso()))
        volumenes = math.ceil(sumaVolumenes / float(self.mochila.getVolumen()))
        if(pesos >= volumenes):
            return pesos
        else:
            return volumenes

    def generarRestricciones(self):
        self.generarRestriccionesTipo(self.primeraRestriccion, 1)
        self.generarRestriccionesTipo(self.segundaRestriccion, 0)
        self.generarRestriccionesTipo(self.terceraRestriccion, 2)

    def printMatrix(self,testMatrix):
        for i in range(len(testMatrix)):
            for j in range(len(testMatrix[i])):
                print(testMatrix[i][j], end=" ")
            print()
        print()

    def getNumPersonas():
        return self.optimumNumberPeople