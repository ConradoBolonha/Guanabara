"""
Crie um jogo que faça o computador jogar Jokenpô com você.
"""
from random import randint

print ('\n{:*^40}'.format(' JOGO DE JOKENPÔ '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''\nSua opções são: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('\nQual é a sua jogada? '))
print('=-' * 13)
print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
print('=-' * 13)
if computador == 0: #  PEDRA
    if jogador == 0: #  PEDRA
        print('EMPATE')
    elif jogador == 1: #  PAPEL
        print('O JOGADOR VENCEU')
    elif jogador == 2: #  TESOURA
        print('O COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA')
    
elif computador == 1: #  PAPEL
    if jogador == 0: #  PEDRA
        print('O COMPUTADOR VENCEU')
    elif jogador == 1: #  PAPEL
        print('EMPATE')
    elif jogador == 2: #  TESOURA
        print('O JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: #  TESOURA
    if jogador == 0: #  PEDRA
        print('O JOGADOR VENCEU')
    elif jogador == 1: #  PAPEL
        print('O COMPUTADOR VENCEU')
    elif jogador == 2: #  TESOURA
        print('EMPATE')
    else:
        print ('JOGADA INVÁLIDA')
