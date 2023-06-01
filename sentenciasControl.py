"""
#Intrucción If

num = int(input('Ingrese un número: '))

if num != 0:
    if num > 0: 
        if num % 2 == 0:
            print(f'El número {num} es par Positivo')
        else:
            print(f'El número {num} es impar Positivo')
    elif num % 2 == 0:
        print(f'El número {num} es par Negativo')
    else:
        print(f'El número {num} es impar Negativo')
else:
    print(f'El número {num} es neutro')
"""

"""
#Instrucción elif
vocal = input('Ingrese un dato:')

if vocal == 'a':
    print(vocal, 'Es vocal')
elif vocal == 'e':
    print(vocal, 'Es vocal')
elif vocal == 'i':
    print(vocal, 'Es vocal')
elif vocal == 'o':
    print(vocal, 'Es vocal')
elif vocal == 'u':
    print(vocal, 'Es vocal')
else:
    print(vocal, 'No es vocal')
""" 

"""
#While
#Suma de los N primeros números

num = int(input('Ingrese el número: '))
cont = 1
suma = 0
while cont <= num:
    suma += cont
    cont += 1

print(suma)
"""
"""
#Mostrar el número menor de n números ingresados
n = int(input('Cantidad de números:'))
menor = 0
i = 1
while (i <= n):
    numero = int(input('Número: '))
    if (i == 1):
        menor = numero
    elif numero < menor:
        menor = numero    
    i += 1

print(f'El número menor es: {menor}')
"""

#For
palabras = ['Gato', 'León', 'Avión', 'Auto']
for p in palabras:
    print(p, len(p))
    
for i in range(5):
    print(i)