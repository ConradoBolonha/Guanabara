"""
Crie um jogo que faça o computador jogar Jokenpô com você.
"""
from random import randint
from time import sleep

print ('\n{:*^40}'.format(' JOGO DE JOKENPÔ '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''\nSua opções são: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('\nQual é a sua jogada? '))
#  print('=-' * 13)
print('\nJO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ !!!')
sleep(1)
print('\nO computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
#  print('=-' * 13)
if computador == 0: #  PEDRA
    if jogador == 0: # PEDRA
        print('\n\033[33mEMPATE!!!\033[m')
        print('\n')
    elif jogador == 1: #  PAPEL
        print('\n\033[32mO JOGADOR VENCEU :-)\033[m')
        print('\n')
    elif jogador == 2: # TESOURA
        print('\n\033[31mO JOGADOR PERDEU :-(\033[m')
        print('\n')
    else:
        print('JOGADA INVÁLIDA!!!')
        print('\n')
        
if computador == 1: #  PAPEL
    if jogador == 0: # PEDRA
        print('\n\033[31mO JOGADOR PERDEU :-(\033[m')
        print('\n')
    elif jogador == 1: #  PAPEL
        print('\n\033[33mEMPATE!!!\033[m')
        print('\n')
    elif jogador == 2: #  TESOURA
        print('\n\033[32mO JOGADOR VENCEU :-)\033[m')
        print('\n')
    else:
        print('\nJOGADA INVÁLIDA!!!')
        print('\n')
if computador == 2: #  TESOURA
    if jogador == 0: #  PEDRA
        print('\n\033[32mO JOGADOR VENCEU :-)\033[m')
        print('\n')
    elif jogador == 1: #  PAPEL
        print('\n\033[31mO JOGADOR PERDEU :-(\033[m')
        print('\n')
    elif jogador == 2:
        print('\n\033[33mEMPATE!!!\033[m')
        print('\n')
    else:
        print('\nJOGADA INVÁLIDA!!!')
        print('\n')
