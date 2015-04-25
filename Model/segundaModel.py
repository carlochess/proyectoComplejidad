class SegundaParteModel:

    def __init__(self,descriptionBoxes,volumeBackpack,maximumWeightBackpack):
        from .Item import Item
        from .Mochila import Mochila
        from .lpSolv import resolver

        self.items = []
        self.mochila = None
        for listaCaja in self.descriptionBoxes:
            self.items.append(Item(int(listaCaja[1]),int(listaCaja[2])))
        print(self.items)
        self.mochila=Mochila(volumeBackpack,maximumWeightBackpack)
        print(self.mochila)
        numeroProblema = self.nombreProblema+"_1.lp"
        self.n = len(self.items)#int(self.hallarN())
        self.i = len(self.items)
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
        self.optimumNumberPeople = resolver(self.matriz,self.n,self.i,numeroProblema)

    def setProblemName(self, nombre):
        self.nombreProblema = "0"
        print(self.nombreProblema)

    def generarRestriccionesTipo(self, matriz, tipo):
        numeroRestricciones = (n * ( n - 1 ) ) / 2
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
                    for k in range(0, numeroRestricciones):
                        restriccionCanecaI.append(0)
                    restriccionCanecaI.append("<=")
                    restriccionCanecaI.append(caneca.getPeso())
                elif tipo == 1:
                    for k in range(0, numeroRestricciones):
                        restriccionCanecaI.append(0)
                    restriccionCanecaI.append("<=")
                    restriccionCanecaI.append(caneca.getVolumen())
                matriz.append(restriccionCanecaI)
        elif tipo == 2:
            for j in range(0, i):
                restriccionCanecaI = []
                for k in range(0, i * n + numeroRestricciones):
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

    def generarFuncObj(self, matriz):
        restriccionCanecaI = []
        numeroRestricciones = (n* (n-1)) / 2
        for k in range(0, i * n):
            restriccionCanecaI.append(0)
        for k in range(0, numeroRestricciones):
            restriccionCanecaI.append(1)
        matriz.append(restriccionCanecaI)


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
        generarRestriccionesTipo(primeraRestriccion, 1)
        generarRestriccionesTipo(segundaRestriccion, 0)
        generarRestriccionesTipo(terceraRestriccion, 2)
        generarRestriccionesTipo(cuartaRestriccion, 3)

    def printMatrix(self,testMatrix):
        for i in range(len(testMatrix)):
            for j in range(len(testMatrix[i])):
                print(testMatrix[i][j], end=" ")
            print()
        print()

    def getNumPersonas():
        return self.optimumNumberPeople