# Métodos para manipular cadenas str
""""
def get_string_metodos():
    i = 0
    for metodo in dir(str):
        if '__' not in metodo:
            i += 1
            print(i, metodo, sep=':')

get_string_metodos()


# 1. Capitalize
text = 'grover'
print(text.capitalize())

# 2. casefold
text = 'Grover'
print(text.casefold())

# 3. center
text = 'Grover'
print(text.center(50, '-'))

# 4. count
text = 'abc_ab_abd_acd_abr'
print(text.count('ab'))

# 5. endswith
text = 'abc_cde_grover'
print(text.endswith('er'))

# 6. expandtabs
text = 'abc\tabc\tabc'
print(text.expandtabs(30))

# 7. find, rfind
texto = 'Grover Vasquez abc'
posicion = texto.rfind('quez')
print(posicion)
print(texto[posicion:])


# 8. format
text = '{asunto} al canal {accion}'
print(text.format(asunto='Suscríbete', accion='ahora'))

text = '{} al canal {}'
print(text.format('Suscríbete', 'ahora'))


# 9. format_map
coordenadas = {'x': 60, 'y': 20}
text = 'Coordenadas: {x}, {y}'
print(text.format_map(coordenadas))


# 10. index
text = 'Grover Vasquez'
print(text.index('V'))


# 11. isdecimal
text = '123'
print(text.isdecimal())

# 12. isdigit
text = '①②③'
print(text.isdigit())

# 13. isnumeric
text = '一二三123'
print(text.isnumeric())


# 14. islower, isupper. 
text = 'GROVER'
print(text.isupper())
print(text.islower())


# 15. istitle
text = 'La Película Transformers'
print(text.istitle())


#16. lower, upper
text = 'GrovEr'
print(text.lower())
print(text.upper())


#17. join
text = '-'
print(text.join(['texto1', 'texto2', 'texto3']))

# 18. ljust, rjust
text = 'Grover'
print(text.rjust(20, '_'))


# 19. lstrip, rstrip
text = 'Suscríbete ahora'
print(text.rstrip('ora'))


# 20. translate, maketrans
text = 'Prueba ahora'
table = text.maketrans('o', '5')
print(table)
print(text.translate(table))


# 21. partition
text = 'a+b=c=D'
print(text.partition('='))


# 22. removesuffix, removepreffix
text = 'WhatApp'
print(text.removeprefix('What'))
print(text.removesuffix('App'))


# 23. replace
text = 'Recuerda dejar tu comentario'
print(text)
print(text.replace('comentario', 'suscripcion'))
"""

# 24. split, lsplit, rsplit
text = 'Esto es una prueba de split'
print(text.split(sep=' ', maxsplit=2))