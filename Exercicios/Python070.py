'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final,
mostre:

a) Qual é o total gasto na compra;
b) Quantos produtos custam mais de R$ 1.000,00;
c) Qual é o nome do produto mais barato.
'''

while True:
    nome_prod = str(input('Digite o nome do produto: '))
    valor_prod = float(input('Digite o valor: '))
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Incluir mais produtos? [S/N] } ')).strip().upper() [0]
    if resposta == 'N':
        break
print(('\n'), '{:-^40}'.format('FIM'))
