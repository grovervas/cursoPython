class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def getDatos(self):
        print(f'Nombre: {self.nombre} \tEdad: {self.edad}')
    

#Herencia
class Usuario(Persona):
    
    def getDatos(self):
        return 'Datos del usuario', super().getDatos()
        #print(f'Datos del usuario, Nombre: {self.nombre}, Edad:{self.edad}')

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def getDatos(self):
        print(f'Datos des Empleado, {super().getDatos()}, sueldo:{self.sueldo}')
        