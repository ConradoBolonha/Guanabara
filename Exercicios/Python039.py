"""
Faça um programa que leia o ano de nascimento de um jovem e
informe de acordo com sua idade:

1º - Se ele ainda vai se alistar ao serviço militar.
2º - Se é a hora de se alistar.
3º - Se já passou do tempo de alistamento.

Seu programa também deverá mostar o tempo que falta ou
que passou do prazo
"""

ano_nasc = int(input('\nDigite seu ano de nascimento: '))
if 2022 - ano_nasc < 18:
    print('Você ainda não tem idade para se alistar!')
elif 2022 - ano_nasc == 18:
    print('Você tem que que se alistar esse ano.')
elif 2022 - ano_nasc > 18:
    print('Você já passou do tempo de se alistar!')
