menu = '''
Bienvenido al conversor de monedas \U0001f4b0

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: '''

opcion = input(menu)

if opcion == '1':
    pesos_colombinos = input('Cuántos pesos colombianos tienes?: ')
    pesos_colombinos = float(pesos_colombinos)
    valor_dolar = 4580.14
    dolares = pesos_colombinos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
elif opcion == '2':
    pesos_argentinos = input('Cuántos pesos argentinos tienes?: ')
    pesos_argentinos = float(pesos_argentinos)
    valor_dolar = 127.351
    dolares = pesos_argentinos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
elif opcion == '3':
    pesos_mexicanos = input('Cuántos pesos mexicanos tienes?: ')
    pesos_mexicanos = float(pesos_mexicanos)
    valor_dolar = 20.7935
    dolares = pesos_mexicanos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
else:
    print('Ingresa una opción valida')