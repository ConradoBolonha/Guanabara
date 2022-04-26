"""
Faça um programa que leia o ano de nascimento de um jovem e
informe de acordo com sua idade:

1º - Se ele ainda vai se alistar ao serviço militar.
2º - Se é a hora de se alistar.
3º - Se já passou do tempo de alistamento.

Seu programa também deverá mostar o tempo que falta ou
que passou do prazo
"""
from datetime import date

atual = date.today().year
ano_nasc = int(input('\nDigite seu ano de nascimento: '))
idade = atual -ano_nasc

if idade == 18:
    print('Você tem que que se alistar IMEDIATAMENTE!!!.')
    print('Quem nasceu em {} tem {} anos em 2022'.format(ano_nasc, ano_nasc - 2022))
    print('Você está com {} anos e faltam {} anos para se alistar!')
elif ano_nasc < 18:
    print()
elif ano_nasc > 18:
    print('Quem nasceu em {} tem {} anos em 2022'.format(ano_nasc, ano_nasc - 2022))
    print('Você já deveriq ter se alistado em {} anos'.format(ano_nasc - 18))
    print('Você já passou do tempo de se alistar!')
