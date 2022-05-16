'''
Melhore o jogo do desafio 028 onde o computador pensa em um número
entre 0 e 1, só que agora, o jogador vai tentar adivinhar até acertar
mostrando no final quantos palpites foram necessários para vencer.
'''

print('\n== Tente descobrir o número que o computador sorteou ==')
from random import randint
num_comput = (randint(0, 10))
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite um número: '))
    palpite = palpite + 1
    if num_comput == jogador:
        acertou = True
    else:
        if num_comput > jogador:
            print('Tente um número maior!')
        elif num_comput < jogador:
            print('Tente um número menor!')
print('Você acertou com {} tentativas!'.format(palpite))
