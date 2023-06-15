
#Funciones básicas
def saludar(nombre):
    return (f'Hola, {nombre} desde l a función')

#def sumar(a=5, b=10):
#    return a + b

def restar(a, b):
    return a - b

saludo = saludar('Grover')
print(saludo)


resta = restar(b=40, a=80)
print(resta)

#Funciones con argumentos indefinidos
def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    
    return suma, kwargs

suma, datos = sumar(5, 9, 15, 2, 4, 10, ciudad = 'Lima', nombre = 'Grover', edad=42)

print('La suma es:', suma)
print('Datos:', datos)
