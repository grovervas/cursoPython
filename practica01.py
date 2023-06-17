def descuentos(consumo):
    if consumo > 0 and consumo <= 100:
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200:
        descuento = consumo * 0.20
    elif consumo > 200:
        descuento = consumo * 0.30    
    
    return descuento

def impuesto(monto):
    return monto * 0.15

consumo = float(input('Ingrese el consumo del cliente:'))


if(consumo > 0):
    total = consumo - descuentos(consumo)
    totalPago = total + impuesto(total)

    print('Descuento: ', descuentos(consumo))
    print('Total:', total)
    print('Total + IGV:', totalPago)
else:
    print('Dato incorrecto')
