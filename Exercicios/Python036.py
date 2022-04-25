"""
Escreva um programa para aprovar um empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da casa, o
salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo será negado.
"""

vl_casa = input(float('Digite o valor do imóvel: '))
sal = input(float('Digite o valor do salário: '))
tempo_financ = input(int('Tempo de financiamento: '))
valor_financ = vl_casa / tempo_financ
if valor_financ / 0.30 >= sal:
    print('NEGADO. O valor da prestação R$ {} não pode superar 30 por cento do valor do salário'.format(sal))
else:
    print('O valor da prestação será de R$ {}'.format(valor_financ))
