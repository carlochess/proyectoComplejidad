from PyQt4 import QtCore

class Solucionador(QtCore.QThread):

    problemaResuelto = QtCore.pyqtSignal(object)

    def __init__(self, solucion):
        QtCore.QThread.__init__(self)
        self.solucion = solucion

    def run(self):
        self.solucion.resolver()
        self.problemaResuelto.emit('%s\n%s' % (self.url, info))