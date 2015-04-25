#==============================================================================
#==================================Main Model==================================
#==============================================================================
from __future__ import print_function
class MainModel(object):

    def __init__(self,numberBoxes=None,volumeBackpack=None,maximumWeightBackpack=None,
                 descriptionBoxes=None,optimumNumberPeople=None):
        super(MainModel,self).__init__()
        self.numberBoxes=numberBoxes
        self.volumeBackpack=volumeBackpack
        self.maximumWeightBackpack=maximumWeightBackpack
        self.descriptionBoxes=descriptionBoxes
        self.optimumNumberPeople=optimumNumberPeople

    def getNumberBoxes(self):
        return(self.numberBoxes)

    def getVolumeBackpack(self):
        return(self.volumeBackpack)

    def getMaximumWeightBackpack(self):
        return(self.maximumWeightBackpack)

    def getDescriptionBoxes(self):
        return(self.descriptionBoxes)

    def getOptimumNumberPeople(self):
        return(self.optimumNumberPeople)

    def getDataTable(self):
        return({"Box Number":self.listBoxNumber(self.descriptionBoxes),
                "Box Volume":self.listBoxVolume(self.descriptionBoxes),
                "Box Weight":self.listBoxWeight(self.descriptionBoxes)})

    def listBoxNumber(self,dataList):
        newDataList=[]
        for i in range(len(dataList)):
            newDataList.append((str)(dataList[i][0]))
        return(newDataList)

    def listBoxVolume(self,dataList):
        newDataList=[]
        for i in range(len(dataList)):
            newDataList.append((str)(dataList[i][1]))
        return(newDataList)

    def listBoxWeight(self,dataList):
        newDataList=[]
        for i in range(len(dataList)):
            newDataList.append((str)(dataList[i][2]))
        return(newDataList)

    def processingDataList(self,dataList):
        print("input list: ",dataList,"\n")
        numberBoxes=(int)(dataList.pop(0))
        print("number boxes: ",numberBoxes,"\n")
        propertiesBackpack=[]
        cadena=""
        for i in range(len(dataList[0])):
            cadena+=dataList[0][i]
            if((dataList[0][i]==" ")or(i==(len(dataList[0])-1))):
                propertiesBackpack.append((float)(cadena))
                cadena=""
        print("properties backpack: ",propertiesBackpack,"\n")
        dataList.pop(0)
        string=""
        descriptionBoxes=[]
        for i in range(len(dataList)):
            aux=[]
            for j in range(len(dataList[i])):
                string+=dataList[i][j]
                if((dataList[i][j]==" ")or(j==(len(dataList[i])-1))):
                    aux.append((str)(string))
                    string=""
            descriptionBoxes.append([(int)(aux[0]),(float)(aux[1]),(float)(aux[2])])
        print("description boxes: ",descriptionBoxes,"\n")
        self.numberBoxes=numberBoxes
        self.volumeBackpack=propertiesBackpack[0]
        self.maximumWeightBackpack=propertiesBackpack[1]
        self.descriptionBoxes=descriptionBoxes
##################################################3
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

    #Esta funcion calcula el numero optimo de personas en este caso seria 10
    def calculateOptimalNumberPeople(self):
        from .Item import Item
        from .Mochila import Mochila
        from .lpSolv import resolver

        self.items = []
        self.mochila = None
        for listaCaja in self.descriptionBoxes:
            self.items.append(Item(int(listaCaja[1]),int(listaCaja[2])))
        print(self.items)
        self.mochila=Mochila(self.volumeBackpack,self.maximumWeightBackpack)
        print(self.mochila)
        numeroProblema = "1_1.lp"
        self.n = int(self.hallarN())
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
#==============================================================================