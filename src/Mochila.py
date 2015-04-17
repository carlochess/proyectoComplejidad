from Objeto import Objeto
class Mochila(Objeto):
    def __init__(self, volumen, peso ):
        Objeto.__init__(self, volumen,peso)
    def __str__(self):
        return str(self.peso)+" "+str(self.volumen)
