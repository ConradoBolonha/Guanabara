'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte. Seu programa
deverá ler um número pelo teclado (0 a 20) e mostra-lo por
extenso.

Desafio: Faça com que o programa pergunte se deseja continuar ou não.
'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete',
'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Opção inválida! Tente novamente.')
    print(f'Por extenso, o número é {contagem[numero]}.')
    while True:
        resposta = str(input('Quer continuiar? [S/N] ')).upper().strip()[0]
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
print(' *** FIM ***')
