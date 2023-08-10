from io import open

try:
    with open('./tmp/data.txt', mode='r', encoding='utf-8') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('Archivo no existe.')
    raise err

