from Objeto import Objeto
class Mochila(Objeto):
    def __init__(self, peso, volumen):
        Objeto.__init__(self, peso, volumen)
	def __str__(self):
		return str(self.peso)+" "+str(self.volumen)
