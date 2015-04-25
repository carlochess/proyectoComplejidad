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
    #Esta funcion calcula el numero optimo de personas en este caso seria 10
    def calculateOptimalNumberPeople(self):
        from .primeraModel import PrimeraParteModel
        p = PrimeraParteModel()
        self.optimumNumberPeople = p.getNumPersonas(self.descriptionBoxes,self.volumeBackpack,self.maximumWeightBackpack)

    #Esta funcion calcula el numero optimo de personas en este caso seria 10
    def calculateEquitativeNumberPeople(self):
        from .segundaModel import SegundaParteModel
        p = SegundaParteModel()
        self.optimumNumberPeople = p.getNumPersonas(self.descriptionBoxes,self.volumeBackpack,self.maximumWeightBackpack)

    def generarGrafico(self):
        import numpy as np
        import matplotlib.pyplot as plt

        N = 5
        menMeans = (20, 35, 30, 35, 27)
        menStd =   (2, 3, 4, 1, 2)

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

        womenMeans = (25, 32, 34, 20, 25)
        womenStd =   (3, 5, 2, 3, 3)
        rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

        ax.set_ylabel('Valoes')
        ax.set_title('Valores por volumen y peso')
        ax.set_xticks(ind+width)
        ax.set_xticklabels( ('M0', 'M1', 'M2', 'M3', 'M4') )

        ax.legend( (rects1[0], rects2[0]), ('Volumen', 'Peso') )

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.show()
#==============================================================================