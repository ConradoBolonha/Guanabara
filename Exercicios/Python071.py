'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de
cada valor serão entregues.

Obs: Considere que o caixa possui cédulas
de R$ 50,00 / R$ 20,00 / R$ 10,00 / R$ 5,00 / R$ 1,00 
'''
print('=' * 29)
print('{:^30}'.format('SIMULADOR DE CAIXA ELETRÔNICO'))
print('=' * 29)
valor = int(input('Digite o valor do saque: R$ '))
total = valor
cedula = 50
total_ced = 0
while True:
    if total >= cedula:
        total -= cedula
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        total_ced = 0
        if total == 0:
            break
print('\n','*** SESSÃO ENCERRADA ***')
