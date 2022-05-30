'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois
disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
'''

from random import randint
num_sortidos = randint(1, 10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
print(f'Os valores sorteados foram: ', end='')
for numeros in num_sortidos:
    print((f'{numeros}'), end=' ')
print(f'\nO maior valor sorteado foi {max(num_sortidos)} e o menor é {min(num_sortidos)}.')
