
while True:
    try:
        edad = int(input('¿Cuál es tu edad?:'))
        div = 10/edad
        print(edad)
    except ValueError as err:
        print('Error:, ', err)
        continue
    except ZeroDivisionError as err:
        print('Error:', err)
        break
    else:
        print('Gracias!')
        break
    finally:
        print('Se acabo el programa.')
