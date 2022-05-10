"""
Crie um programa que leia o ano de nascimento de sete pessoas e
que no final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são de maior.
"""

from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0
for pessoas in range (1, 8):
    ano_nasc = int(input('Digite o ano de nascimentoda {}ª pessoa: '.format(pessoas)))
    idade = ano_atual - ano_nasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print('A maioridade NÃO foi atingida por {} pessoas!'.format(total_menor))
print('{} pessoas atingiram a maioridade!'.format(total_maior))
