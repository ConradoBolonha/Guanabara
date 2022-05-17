'''
Faça um programa que leia um número qualquer e mostre o
seu fatorial.

Exemplo: 5! = 5x4x3x2x1 = 120
'''
'''
print('\n=== CALCULANDO O FATORIAL DE UM NÚMERO ===')
from math import factorial
numero = int(input('\nDigite um número: '))
fatorial = factorial(numero)
print('O fatorial de {} é {}.\n'.format(numero, fatorial))
'''

print('\n=== CÁLCULO DO FATORIAL DE UM NÚMERO ===')
numero = int(input('\nDigite um número: '))
contador = numero
fatorial = 1
print('\nO fatorial de {} ='.format(numero), end = ' ')
while contador > 0:
    print('{}'.format(contador), end = ' ')
    print('x ' if contador > 1 else '=', end = '')
    fatorial = fatorial * contador
    contador = contador - 1
print(' {}'.format(fatorial), '\n')
