"""
Faça um programa que leia um número inteiro e diga se ele
é ou não um número primo.
"""

NumPrimo = int(input('Digite um número: '))
total = 0
for cont in range(1, NumPrimo + 1):
    if NumPrimo % cont == 0:
        print('\033[31m', end = ' ')
        total += 1
    else:
        print('\033[36m', end = ' ')
    print('{}'.format(cont), end = ' ')
print('\nO número {} foi divisível por {}.'.format(NumPrimo, total))
if total ==2:
    print('O número {} É primo!'.format(NumPrimo))
else:
    print('O número {} NÃO é primo!'.format(NumPrimo))
