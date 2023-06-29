from poo import Persona

#Instancias de la clase Persona
per1 = Persona('Grover', 40, 999123456) 
per2 = Persona('Pablo', 29, 987654321)
per3 = Persona('Ana', 25, 678987654)
per4 = Persona(None, None, None)

per2.getDatos()
print('='*10)
per1.getDatos()
print('='*10)
per3.getDatos()
print('='*10)
per4.getDatos()