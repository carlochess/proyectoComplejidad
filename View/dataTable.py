#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#==============================================================================


#==============================================================================
#=======================Create Table Data To Be Displayed======================
#==============================================================================
class Table(QTableWidget):

    def __init__(self,data,*args):
        QTableWidget.__init__(self,*args)
        self.data=data
        self.setData()
        self.resizeColumnsToContents()
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.resizeRowsToContents()

    def setData(self):
        horHeaders=[]
        for i,key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for j,item in enumerate(self.data[key]):
                newitem=QTableWidgetItem(item)
                #newitem.setTextAlignment(Qt.AlignCenter)
                self.setItem(j,i,newitem)
        self.setHorizontalHeaderLabels(horHeaders)

    def asignarItemsaMochilas(self,solucion):
        for i in range(self.rowCount()):
            newitem=QTableWidgetItem(str(solucion.getItem(i).getMochila()))
            self.setItem(i,0,newitem)
#==============================================================================
