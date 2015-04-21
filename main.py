#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
import sys
from PyQt4.QtGui import QApplication
from Model import mainModel
from Controller import mainController
#==============================================================================


#==============================================================================
#==================================Main Class==================================
#==============================================================================
class Main(QApplication):
    def __init__(self,sys_argv):
        super(Main,self).__init__(sys_argv)
        self.appModel=mainModel.MainModel()
        self.appController=mainController.MainController(self.appModel)

if(__name__=="__main__"):
    app=Main(sys.argv)
    sys.exit(app.exec_())
#==============================================================================