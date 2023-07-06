class Persona:
    
    __nombre = None
    __edad = None
    
    def __init__(self, nom, ed, mov):
        self.__nombre = nom
        self.__edad = ed
        self._movil = mov
    
    def getDatos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)    
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_edad(self, edad):
        self.__edad = edad 