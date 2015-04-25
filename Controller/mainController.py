#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
from __future__ import print_function
import sys
sys.path.append("..")
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from View import mainWindow
from View import dataTable
#==============================================================================


#==============================================================================
#===============================Main Controller================================
#==============================================================================
class MainController(object):

    def __init__(self,appModel):
        self.appModel=appModel
        self.window=mainWindow.MainWindow(self.appModel,self)
        self.window.show()

    def functionExit(self):
        self.window.close()

    def functionOpenFile(self):
        directory="DataInput"
        try:
            fileName=QFileDialog.getOpenFileName(self.window,"Abrir archivo",directory)
            with open(fileName,"r") as fileContent:
                dataList=[line.rstrip("\n") for line in fileContent]
            self.appModel.setProblemName(fileName)
            self.appModel.processingDataList(dataList)
        except:
            pass
        self.window.newWidgetsOne()
        self.initializeWindow()

    def functionRandom(self):
        from random import randint
        from os import listdir
        from os.path import isfile, join
        archivos = sorted([ f for f in listdir("DataInput") if isfile(join("DataInput",f)) ])
        if len(archivos) == 0:
            nombre = "0"
        else:
            nombre = int(archivos[-1])+1
        fileName = "DataInput/"+str(nombre)
        f = open(fileName,'w')
        nCajas = randint(2,6)
        f.write(str(nCajas)+"\n")
        vMaleta = randint(2,200)
        pMaleta = randint(2,200)
        f.write(str(vMaleta)+" "+str(pMaleta)+"\n")
        for i in range(nCajas):
            nCaja = i
            vCaja = randint(1,vMaleta)
            pCaja = randint(1,pMaleta)
            f.write(str(nCaja)+" "+str(vCaja)+" "+str(pCaja)+"\n")
        f.close()
        with open(fileName,"r") as fileContent:
            dataList=[line.rstrip("\n") for line in fileContent]
        #self.appModel.setProblemName(nombre)
        self.appModel.processingDataList(dataList)
        self.window.newWidgetsOne()
        self.initializeWindow()

    def functionHelp(self):
        QMessageBox.question(self.window, "Help - Complexity and Optimization",
        """
        ========================================================

        Description of problem:

        The problem consists of two parts. In the first part asks for the optimal
        amount of persons responsible for carrying first aid items to a place where
        a disaster occurred; in the second part you want to distribute the load
        optimally. It should solve the first part, the optimal number of people
        is parameter in the solution of the second part.

        ========================================================
        """)

    def functionAbout(self):
        QMessageBox.information(self.window, "About - Complexity and Optimization",
        """
        ========================================================

        Complexity and Optimization has been developed by Carlos Roman, Sebastian
        Narvaez and Sebastian Rodriguez with Python programming language in
        Version 3.4, implements the QT4 library in Version 4.11 to generate its
        GUI. For more information write to email rodrigueztrujillojuan@hotmail.com

        ========================================================
        """)

    def calculateFirstOptimization(self):
        self.appModel.calculateOptimalNumberPeople()
        self.window.lineEditFour.setText((str)(self.appModel.getOptimumNumberPeople()))

    def createDataTable(self):
        return(dataTable.Table(self.appModel.getDataTable(),self.appModel.getNumberBoxes(),3))

    def initializeWindow(self):
        self.window.lineEditOne.setText((str)(self.appModel.getNumberBoxes()))
        self.window.lineEditTwo.setText((str)(self.appModel.getMaximumWeightBackpack()))
        self.window.lineEditThree.setText((str)(self.appModel.getVolumeBackpack()))
#==============================================================================
