'''
Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que o jogador conquistou no
final do jogo.
'''

from random import randint
print('\n')
print('=-' * 13)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 13, '\n')
vitoria = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI': # "PI" = Par ou ímpar
        tipo = str(input('PAR ou ÍMPAR ? ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}.')
    print(f'A soma deu {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            vitoria += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
            vitoria += 1
        else:
            print('Você perdeu!!!')
            break
    print(f'Vamos jogar novamente...')
print(f'FIM DO JOGO! Você ganhou {vitoria} vezes.')
