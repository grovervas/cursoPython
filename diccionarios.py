
#Diccionarios
personas = ['Grover', 40, 1.75]

persona = {
    'nombre': 'Grover',
    'edad': 40,
    'size': 1.75,
    'gadget': ['iPhone', 'iPad', 'Audifono'],
    'casado': True
}
#persona['direccion'] = 'Lima'

lista = persona['gadget']
#print(persona.get('edad', 35))
#persona.clear()
#print(persona.keys())
#print(persona.values())
#print(persona.items())
#persona.pop('edad')
persona.update({'mascota': False})
#print(persona)
#for k, v in persona.items():
#    print(k, v)
#print(len(persona))

#Tuplas
tupla = (123, 'Grover', 40, 1.75, 'Grover', 123)
#print(len(tupla))

#Set (Conjuntos)
conja = set('abracadabra')
conjb = set('alacazam')
#print(conja)
#print(conjb)
#print(conjb - conja)
#print(conja | conjb)
#print(conja & conjb)
#print(conja ^ conjb)

c = {'perro', 'gato', 'gallina'}
d = {'apple', 'gato', 'google'}
x = c.difference(d)
c.discard('perro')
d.pop()
d.update(c)
print(d)