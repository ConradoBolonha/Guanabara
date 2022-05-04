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
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
print('\nO computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
print('=-' * 13)
if computador == 0: #  PEDRA1
        print('\nO JOGADOR VENCEU :-)')
    elif jogador == 2: #  TESOURA
        print('\nO COMPUTADOR GANHOU :-(')
    else:
        print('\nJOGADA INVÁLIDA')
    
elif computador == 1: #  PAPEL
    if jogador == 0: #  PEDRA
        print('\nO COMPUTADOR VENCEU :-(')
    elif jogador == 1: #  PAPEL
        print('\nEMPATE')
    elif jogador == 2: #  TESOURA
        print('\nO JOGADOR VENCEU :-)')
    else:
        print('\nJOGADA INVÁLIDA')

elif computador == 2: #  TESOURA
    if jogador == 0: #  PEDRA
        print('\nO JOGADOR VENCEU :-)')
    elif jogador == 1: #  PAPEL
        print('\nO COMPUTADOR VENCEU :-(')
    elif jogador == 2: #  TESOURA
        print('\nEMPATE')
    else:
        print ('\nJOGADA INVÁLIDA')
