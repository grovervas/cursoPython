import math
class Figura:
    area = None
    perimetro = None
    
    def __init__(self):
        pass
    
    def calcularArea(self):
        pass
    
    def calcularPerimetro(self):
        pass
    
class Circulo(Figura):
    def __init__(self, radio):
        self.nombre = __class__.__name__
        self.radio = radio
    
    def calcularArea(self):
        self.area = math.pi * self.radio * self.radio
    
    def calcularPerimetro(self):
        self.perimetro = 2 * math.pi * self.radio
    
    def __str__(self):
        return f'{self.nombre}, radio:{self.radio}'

class Cuadrado(Figura):
    def __init__(self, lado):
        self.nombre = __class__.__name__
        self.lado = lado
    
    def calcularArea(self):
        self.area = self.lado * self.lado
    
    def calcularPerimetro(self):
        self.perimetro = 4 * self.lado
    
    def __str__(self):
        return f'{self.nombre}, lado:{self.lado}'

def mostrarDatos(figura):
    figura.calcularArea()
    figura.calcularPerimetro()
    print(figura)       
    print('Area:', figura.area)
    print('Perimetro:', figura.perimetro)
    