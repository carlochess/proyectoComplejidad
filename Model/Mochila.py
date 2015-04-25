from .Objeto import Objeto
class Mochila(Objeto):
    def __init__(self, volumen, peso ):
        Objeto.__init__(self, volumen,peso)
        self.volumenContenido = 0
        self.pesoContenido = 0
    def __str__(self):
        return str(self.volumen)+" "+str(self.peso)

    def setPesoContenido(self, peso):
        self.pesoContenido = peso

    def addPeso(self, peso):
        self.pesoContenido = self.pesoContenido+peso

    def setVolumenContenido(self, volumen):
        self.volumenContenido = volumen

    def addVolumen(self, volumen):
        self.volumenContenido = self.volumenContenido+volumen

    def getVolumenContenido(self):
        return self.volumenContenido

    def getPesoContenido(self):
        return self.pesoContenido
