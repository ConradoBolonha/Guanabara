'''
Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros
elementos de uma Sequência de Fibonacci.

Exemplo: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
print('\n', '=-' * 8, 'SEQUÊNCIA DE FOBONATTI', '=-' * 8)
n = int(input('\nDigite a quantidade de termo Fibonacci: '))
termo_1 = 0
termo_2 = 1
print('~' * 15)
print('{} -> {}'.format(termo_1, termo_2), end = '')
contador = 3
while contador <= n:
    termo_3 = termo_1 + termo_2
    print(' -> {}'.format(termo_3), end = '')
    termo_1 = termo_2
    termo_2 = termo_3
    contador = contador + 1
print(' -> FIM')
