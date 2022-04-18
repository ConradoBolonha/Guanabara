"""
    Escreva um programa que faça o computador calcular em um inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep
num = int(input("\nAdvinhe o número que pensei entre 0 e 5: "))
num_aleat = (randint(0, 5))
print('Processando...')
sleep(2)
print('O número que pensei foi {}.'.format(num_aleat))
if num == num_aleat:
    print('Você acertou!!!')
else:
    print('Errou! Tente novamente.')
print('=-' * 15)
