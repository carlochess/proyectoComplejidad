#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
import sys
sys.path.append("..")
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#==============================================================================


#==============================================================================
#=================================Main Window==================================
#==============================================================================
class MainWindow(QMainWindow):

    def __init__(self,appModel,appController):
        super(MainWindow,self).__init__()
        self.appModel=appModel
        self.appController=appController
        self.initWindow()
        self.initWidgets()
        self.initToolbar()
        self.initMenu()
        self.initStatusBar()
        self.initSignals()

    #==========================================================================
    #==================================Window==================================
    #==========================================================================
    def initWindow(self):
        self.setWindowTitle(self.tr("Complexity and Optimization"))
        self.setWindowIcon(QIcon("Image/Logo.ico"))
        self.setMinimumSize(700,550)
        self.centerWindow()

    def centerWindow(self):
        window=self.frameGeometry()
        centerPoint=QDesktopWidget().availableGeometry().center()
        window.moveCenter(centerPoint)
        self.move(window.topLeft())

    #==========================================================================
    #==================================Widgets=================================
    #==========================================================================
    def initWidgets(self):
        self.botonExit=QAction("Exit",self)
        self.botonExit.setIcon(QIcon("Image/Exit.ico"))
        self.botonExit.setShortcut("Ctrl+Q")
        self.botonExit.setStatusTip(self.trUtf8("Exit the application."))

        self.botonOpenFile=QAction("Open File",self)
        self.botonOpenFile.setIcon(QIcon("Image/OpenFile.ico"))
        self.botonOpenFile.setShortcut("Ctrl+E")
        self.botonOpenFile.setStatusTip(self.trUtf8("Open the file with the input data."))

        self.botonRandom=QAction("Random",self)
        self.botonRandom.setIcon(QIcon("Image/Dice.ico"))
        self.botonRandom.setShortcut("Ctrl+D")
        self.botonRandom.setStatusTip(self.trUtf8("Random file generator."))

        self.botonGrafico=QAction("Grafico",self)
        self.botonGrafico.setIcon(QIcon("Image/Grafico.ico"))
        self.botonGrafico.setShortcut("Ctrl+G")
        self.botonGrafico.setStatusTip(self.trUtf8("Solution plot generator."))

        self.botonHelp=QAction("Help",self)
        self.botonHelp.setIcon(QIcon("Image/Help.ico"))
        self.botonHelp.setShortcut("Ctrl+N")
        self.botonHelp.setStatusTip(self.trUtf8("Application help."))

        self.botonAbout=QAction("About",self)
        self.botonAbout.setShortcut("Ctrl+M")
        self.botonAbout.setStatusTip(self.trUtf8("About the application."))

    def newWidgetsOne(self):
        self.initLabel()
        self.initLineEdit()
        self.initGroupBox()
        self.initGridLayout()
        self.signals()
        self.controlGroupOne.setLayout(self.controlLayout)
        self.mainWidget=QWidget(self)
        mainLayout=QVBoxLayout(self.mainWidget)
        mainLayout.addWidget(self.controlGroupOne)
        self.controlGroupTwo.setLayout(self.controlLayoutTwo)
        mainLayout.addWidget(self.controlGroupTwo)
        self.controlGroupThree.setLayout(self.controlLayoutThree)
        mainLayout.addWidget(self.controlGroupThree)
        self.mainWidget.setFocus()
        self.setCentralWidget(self.mainWidget)

    #==========================================================================
    #==================================Toolbar=================================
    #==========================================================================
    def initToolbar(self):
        self.toolbar=QToolBar(self)
        self.toolbar.addAction(self.botonExit)
        self.toolbar.addAction(self.botonOpenFile)
        self.toolbar.addAction(self.botonRandom)
        self.toolbar.addAction(self.botonGrafico)
        self.toolbar.addAction(self.botonHelp)
        self.addToolBar(self.toolbar)

    #==========================================================================
    #===================================Menu===================================
    #==========================================================================
    def initMenu(self):
        menu=self.menuBar()

        fileMenu=menu.addMenu("File")
        fileMenu.addAction(self.botonOpenFile)
        fileMenu.addAction(self.botonExit)

        helpMenu=menu.addMenu("Help")
        helpMenu.addAction(self.botonHelp)
        helpMenu.addAction(self.botonAbout)

    #==========================================================================
    #===================================Label==================================
    #==========================================================================
    def initLabel(self):
        self.labelOne=QLabel("Number of Boxes:")
        self.labelTwo=QLabel("Volume of a Backpack:")
        self.labelThree=QLabel("Maximum Weight of a Backpack:")

    #==========================================================================
    #=================================LineEdit=================================
    #==========================================================================
    def initLineEdit(self):
        self.lineEditOne=QLineEdit()
        self.lineEditOne.setToolTip("Number of Boxes")
        self.lineEditOne.setStatusTip(self.trUtf8("Volume of a backpack."))

        self.lineEditTwo=QLineEdit()
        self.lineEditTwo.setToolTip("Maximum Weight of a Backpack")
        self.lineEditTwo.setStatusTip(self.trUtf8("Maximum weight of a backpack."))

        self.lineEditThree=QLineEdit()
        self.lineEditThree.setToolTip("Volume of a Backpack")
        self.lineEditThree.setStatusTip(self.trUtf8("Volume of a backpack."))

        self.lineEditFour=QLineEdit()
        self.lineEditFour.setToolTip("Optimum Number of People")
        self.lineEditFour.setStatusTip(self.trUtf8("Optimum number of people."))

        self.lineEditFifth=QLineEdit()
        self.lineEditFifth.setToolTip("Equitativo")
        self.lineEditFifth.setStatusTip(self.trUtf8("Equitativo."))

    #==========================================================================
    #==================================Button==================================
    #==========================================================================
    def initButton(self):
        self.botonOne=QPushButton("Solucion 1",self)
        self.botonOne.setToolTip("Calculating the Optimum Number of People")
        self.botonOne.setStatusTip(self.trUtf8("Calculating the optimum number of people."))

        self.botonTwo=QPushButton("Solucion 2",self)
        self.botonTwo.setToolTip("Calculating the Optimum Number of People")
        self.botonTwo.setStatusTip(self.trUtf8("Calculating the optimum number of people."))

    #==========================================================================
    #=================================GroupBox=================================
    #==========================================================================
    def initGroupBox(self):
        self.controlGroupOne=QGroupBox("Input Data")
        self.controlGroupTwo=QGroupBox("Description of the boxes")
        self.controlGroupThree=QGroupBox("Output Data")

    #==========================================================================
    #================================GridLayout================================
    #==========================================================================
    def initGridLayout(self):
        self.initButton()
        self.dataTable=self.appController.createDataTable()
        self.controlLayout=QGridLayout()
        self.controlLayoutTwo=QGridLayout()
        self.controlLayoutThree=QGridLayout()

        self.controlLayout.addWidget(self.labelOne,0,0)
        self.controlLayout.addWidget(self.labelThree,1,0)
        self.controlLayout.addWidget(self.lineEditOne,0,1)
        self.controlLayout.addWidget(self.lineEditTwo,1,1)
        self.controlLayout.addWidget(self.labelTwo,0,2)
        self.controlLayout.addWidget(self.lineEditThree,0,3)
        self.controlLayoutTwo.addWidget(self.dataTable,0,0)
        self.controlLayoutThree.addWidget(self.botonOne,0,0)
        self.controlLayoutThree.addWidget(self.botonTwo,1,0)
        self.controlLayoutThree.addWidget(self.lineEditFour,0,1)
        self.controlLayoutThree.addWidget(self.lineEditFifth,1,1)

    #==========================================================================
    #================================Status Bar================================
    #==========================================================================
    def initStatusBar(self):
        self.setStatusBar(QStatusBar())

    #==========================================================================
    #==================================Signals=================================
    #==========================================================================
    def initSignals(self):
        self.connect(self.botonExit,SIGNAL("triggered()"),self.appController.functionExit)
        self.connect(self.botonOpenFile,SIGNAL("triggered()"),self.appController.functionOpenFile)
        self.connect(self.botonGrafico,SIGNAL("triggered()"),self.appController.functionGrafico)
        self.connect(self.botonRandom,SIGNAL("triggered()"),self.appController.functionRandom)
        self.connect(self.botonHelp,SIGNAL("triggered()"),self.appController.functionHelp)
        self.connect(self.botonAbout,SIGNAL("triggered()"),self.appController.functionAbout)

    def asignarItemsaMochilas(self, solucion):
        self.dataTable.asignarItemsaMochilas(solucion)

    def signals(self):
        self.connect(self.botonOne,SIGNAL("clicked()"),self.appController.calculateFirstOptimization)
        self.connect(self.botonTwo,SIGNAL("clicked()"),self.appController.calculateSecondOptimization)
#==============================================================================
