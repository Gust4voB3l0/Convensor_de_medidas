# Escreva um programa que leia um valor em metros e converta ele para centímetros e milímetros

metro1 = int(input('Digite um valor em metros: '))

# convertendo o valor em centímetros

centimetros = metro1 * 100

# Convertendo o valor em milímetros

milimetros = metro1 * 1000
print('O valor {} em centimetros é {}cm, e em milimetros é {}mm'.format(metro1, centimetros, milimetros))
