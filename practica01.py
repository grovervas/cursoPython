consumo = float(input('Ingrese el consumo del cliente:'))

if consumo > 0 and consumo <= 100:
    descuento = consumo * 0.10
elif consumo > 100 and consumo <= 200:
    descuento = consumo * 0.20
elif consumo > 200:
    descuento = consumo * 0.30
else: 
    descuento = 0
    print('Consumo invalido')

if(consumo > 0):
    total = consumo - descuento
    totalPago = total + total * 0.15

    print('Descuento: ', descuento)
    print('Total:', total)
    print('Total + IGV:', totalPago)
