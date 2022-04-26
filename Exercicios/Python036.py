"""
Escreva um programa para aprovar um empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da casa, o
salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo será negado.
"""

vl_casa = float(input('\nDigite o valor do imóvel: R$ '))
sal = float(input('Digite o valor do salário: R$ '))
tempo_financ = int(input('Tempo de financiamento: '))
prestacao = vl_casa / (tempo_financ * 12)
excede = sal * 30 / 100
if prestacao <= excede:
    print('O valor da prestação será de R$ {:.2f}'.format(prestacao))
else:
    print('NEGADO. O valor da prestação R$ {:.2f} não pode superar 30 por cento (R$ {:.2f}) do valor do salário'.format(sal, excede))
