from Objeto import Objeto
class Item(Objeto):
    def __init__(self, peso, volumen):
        Objeto.__init__(self, peso, volumen)