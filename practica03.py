import random

numeros_loteria = []

for n in range(0,6):
    numero = random.randint(1, 35)
    
    while numero in numeros_loteria:
        numero = random.randint(1,35)
        
    numeros_loteria.append(numero)

numeros_loteria.sort()
print(numeros_loteria)