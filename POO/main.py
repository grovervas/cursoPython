from poo import Persona
from player import Player
from persona import Persona, Usuario, Empleado

"""
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('Hola'))
print(type([]))
print(type(()))
print(type({}))


#Instancias de la clase Persona
per1 = Persona('Grover', 40, 999123456) 
per2 = Persona('Pablo', 29, 987654321)

per2.getDatos()
print('='*10)
per1.getDatos()

player3 = Player()

print(player1.nombre)
print(Player.menbresia)
print(player3.nombre)
print(Player.agregar_datos(1000))
print(Player.agregar_datos2(2000))

player1 = Player('Grover', 40)
player2 = Player('Cindy', 30)

player1.score = 1800

player1.nombre = 'Pablo'
print(player1.nombre)
print(player2.nombre)
print(player1.score)
print(player2.score)


#Acceso a los miembros de la clase
per1 = Persona('Grover', 40, 99999) 
per2 = Persona('Pablo', 29, 123456)

per1.__nombre = 'Ana'

per1.set_nombre('Pedro')
per2.set_edad(32)

print(f"Nombre: {per1.get_nombre()} edad: {per1.get_edad()}")
print(f"Nombre: {per2.get_nombre()} edad: {per2.get_edad()}")
"""
persona = Persona('Grover', 40)
usuario = Usuario('Ana', 30)
empleado = Empleado('Laura', 25, 1500)

usuario.getDatos()
empleado.getDatos()
