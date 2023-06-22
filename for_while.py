
"""
#Enumerate

for i, char in enumerate('Hola'):
    print(i, char)

print(' ')
for i, num in enumerate(list(range(50))):
    print(i, num)
    if (num == 25):
        print(f'index of 25 es: {i}')
"""
#For y While
list = [1, 2, 3]
for i in list:
    print(i)

i = 0
while i <= len(list):
    print(i)
    i += 1
    
