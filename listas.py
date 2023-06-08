productos = ['notebooks', 'lentes', 'iPhones', 'parlantes', 'iphones']

productos[0] = 'laptops'
new_products = productos.copy()
new_products.append('printer')

#new_products.extend(productos)
productos.insert(1,'iPad')

#productos.clear()
#print(productos)
#productos.pop(2)
#print(productos)

if 'parlantes' in productos:
    productos.remove('parlantes')
#print(productos)
#print(productos.index('iphones'))
#print(productos.count('iphones'))

print(new_products)
new_products.sort()
print(new_products)
#print(new_products)