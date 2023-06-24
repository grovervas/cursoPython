imagen = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]    
]

for fila in imagen:
    for pixel in fila:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print(' ')