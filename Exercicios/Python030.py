"""
Crie um programa que leia um número inteiro e mostre na tela se
ele é PAR ou ÍMPAR.

LEMBRANDO QUE O RESTO DA DIVISÃO DE QUALQUER NÚMERO PAR POR DOIS É ZERO
E O RESTO DA DIVISÃO DE QUALQUER NÚMERO ÍMPAR POR DOIS É IGUAL A UM.
"""

num = int(input('\nDigite um número: '))
result = num % 2
if result == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
