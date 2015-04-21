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
        self.resizeRowsToContents()

    def setData(self):
        horHeaders=[]
        for i,key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for j,item in enumerate(self.data[key]):
                newitem=QTableWidgetItem(item)
                self.setItem(j,i,newitem)
        self.setHorizontalHeaderLabels(horHeaders)
#==============================================================================