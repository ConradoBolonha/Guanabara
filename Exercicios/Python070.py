'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final,
mostre:

a) Qual é o total gasto na compra;
b) Quantos produtos custam mais de R$ 1.000,00;
c) Qual é o nome do produto mais barato.
'''

print('-' * 22, '\nLOJAS TEM TUDO', '\n', '-' * 22)
total_prod = total_prod_mil = menor_prod = cont_prod = 0
nome_prod_barato = ' '
while True:
    nome_prod = str(input('Digite o nome do produto: '))
    valor_prod = float(input('Digite o valor: R$ '))
    total_prod += valor_prod
    cont_prod += 1
    if valor_prod > 1000:
        total_prod_mil += 1
    if cont_prod == 1: # Se o contador for o primeiro produto (1 = primeiro produto)
        menor_prod = valor_prod
        nome_prod_barato = nome_prod   
    else:
        if  valor_prod < menor_prod:
            menor_prod = valor_prod
            nome_prod_barato = nome_prod
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Incluir mais produtos? [S/N] ')).strip().upper() [0]
    if resposta == 'N':
        break
print(f'O valor total dos gastos é R$ {total_prod}')
print(f'{total_prod_mil} produtos custam mais de R$ 1.000,00')
print(f'{nome_prod_barato} foi o produto mais barato(R$ {menor_prod}).')
print(('\n'), '{:-^40}'.format('FIM'))
