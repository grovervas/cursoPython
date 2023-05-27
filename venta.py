#Ejemplo de calcular una venta
print("***** HACER UNA VENTA ****")

#Solicitar el precio
precio = float(input("Ingrese el precio:"))

#Operaciones
igv = precio * 0.18
total = precio + igv

#Salida
print('*'*30)
print('***** VENTA *****')
print('*'*30)
print('Valor de la venta:', precio)
print('Impuesto', round(igv,2))
print('Total:', total)
print('*'*30)