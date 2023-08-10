from io import open
from os import path

#Abrir y escribir en el archivo
def escribirArchivo():
    file = open('datos.txt', 'w', encoding='utf-8') #Objeto del tipo File
    file.write('Hola a todos')
    file.close()

def leerArchivo():
    if path.isfile('datos.txt'):
        file = open('datos.txt', 'r', encoding='utf-8')
        #texto = file.read()
        texto = file.readlines()
        print(texto)
        file.close()
    else:
        print('No existe el archivo indicado.')

def agregarDatos():
    if path.isfile('datos.txt'):
        file = open('datos.txt', 'a', encoding='utf-8')
        file.write('\nHola de Nuevo')
        file.close()
    else:
        print('No existe el archivo indicado.')

def modificarArchivo():
    if path.isfile('datos.txt'):
        file = open('datos.txt', 'r+', encoding='utf-8')
        contenido = file.readlines()
        print(contenido)
        contenido[4] = 'Hola Twitch'
        print(contenido)
        eliminarDatos()
        file.seek(0)
        file.writelines(contenido)
        file.close()    
    else:
        print('No existe el archivo indicado.')

def eliminarDatos():
    file = open('datos.txt', 'w', encoding='utf-8')
    file.close()
      
    
#escribirArchivo()
#leerArchivo()
#agregarDatos()
modificarArchivo()
  