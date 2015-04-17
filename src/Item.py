from Objeto import Objeto
class Item(Objeto):
    def __init__(self, volumen, peso ):
        Objeto.__init__(self, volumen,peso)
    def __str__(self):
        return str(self.volumen)+" "+str(self.peso)
    def __repr__(self):
        return str(self.volumen)+" "+str(self.peso)