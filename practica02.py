import random

pares = []
impares = []
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for n in numeros:
    aleatorio = random.randint(1, 100)
    result = n * aleatorio    
    
    if result % 2 == 0:
        pares.append(result)
    else:
        impares.append(result)
        
    print(f'{n} x {aleatorio} = {result}')

print('Lista de Pares: ', pares)
print('Lista de impares: ', impares)