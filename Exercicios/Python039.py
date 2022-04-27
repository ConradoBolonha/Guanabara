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
idade = atual - ano_nasc

if idade < 18:
    print('Você tem {} anos de idade em {}. Faltam {} ano(s) para seu alistamento.\n'.format(idade, atual, 18 - idade))
elif idade == 18:
    print('Você nasceu em {} e tem {} anos em atual. Precisa se alistar IMEDIATAMENTE!!!'.format(ano_nasc, idade, atual))
    print('Você está com {} anos e faltam {} anos para se alistar!\n'.format(idade, 18 - idade))
elif ano_nasc > 18:
    print('Você nasceu em {} e tem {} anos em 2022.'.format(ano_nasc, 2022 - ano_nasc))
    print('O seu alistamento foi no ano de {}.'.format(ano_nasc + 18))
    print('Você já passou do tempo de se alistar!\n')
