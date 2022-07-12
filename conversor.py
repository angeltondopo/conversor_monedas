pesos_colombinos = input('Cuántos pesos colombianos tienes?: ')
pesos_colombinos = float(pesos_colombinos)
valor_dolar = 4580.14
dolares = pesos_colombinos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tienes $' + dolares + ' dólares')