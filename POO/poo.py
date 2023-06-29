class Persona:
       
    def __init__(self, nom, ed, mov):
        self.nombre = nom
        self.edad = ed
        self.movil = mov
    
    def getDatos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)
        print('Móvil: ', self.movil)