def conversor(tipo_moneda, valor_moneda):
    tipo_moneda = input('Cuántos ' + tipo_moneda + ' tienes?: ')
    tipo_moneda = float(tipo_moneda)
    dolares = tipo_moneda / valor_moneda
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')


menu = '''
Bienvenido al conversor de monedas \U0001f4b0

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige tu moneda a convertir: '''

opcion = input(menu)

if opcion == '1':
    conversor('Pesos colombiano', 4490.41)
elif opcion == '2':
    conversor('Pesos argentinos', 127.821)
elif opcion == '3':
    conversor('Pesos mexicanos', 20.7276)
else:
    print('Ingresa una opción valida')