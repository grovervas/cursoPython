class PadreA:
    def __init__(self):
        print('Soy objeto PadreA')
    
    def a(self):
        print('Soy método de PadreA')

class PadreB:
    def __init__(self):
        print('Soy objeto PadreB')
    
    def b(self):
        print('Soy método de PadreB')

class HijoC(PadreA, PadreB):
    def c(self):
        print('Soy médoto de HijoC')
        
#Instancias
hijoc = HijoC()
hijoc.a()
hijoc.b()
hijoc.c()