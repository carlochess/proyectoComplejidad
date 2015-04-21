#==============================================================================
#==================================Main Model==================================
#==============================================================================
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

    #Esta funcion calcula el numero optimo de personas en este caso seria 10
    def calculateOptimalNumberPeople(self):
        print("Calculando optimizacion...")
        self.optimumNumberPeople=10
#==============================================================================