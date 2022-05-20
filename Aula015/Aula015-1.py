'''
contador = 5
while True: #  contador <= 10:
    print(contador)
    contador += 1
print(' FIM ')
'''

numero = 0
soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma = soma + numero
print('A soma é {}.'.format(soma))
