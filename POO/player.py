#Definimos la clase
class Player:
    
    #Atributo de Objeto de clase
    menbresia = True
    
    def __init__(selft, nombre='Anonimo', edad=0):
        selft.nombre = nombre
        selft.edad = edad
    
    def ejecutar(self):
        print('run')
        return 'Ok'
    
    def datos(self):
        print(f'Mi nombre es {self.nombre}')
    
    def getMenbresia(self):
        if Player.menbresia:
            print('Ok')
        else:
            print('No')
    
    @classmethod
    def agregar_datos(cls,score):
        #return score
        return cls('Pedro', 25)
    
    @staticmethod
    def agregar_datos2(score):
        return score
    



