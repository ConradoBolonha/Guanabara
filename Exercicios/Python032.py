"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
"""
Início ano bissexto em vigor: 1582
A cada quatro anos, há um ano bissexto. São bissextos todos os anos múltiplos
de 400, exceto se for múltiplo de 100, mas não de 400, por
exemplo: 1996, 2000, 2004, 2008, 2012, 2016, 2020. Não são bissextos os anos múltiplos
de 100, por exemplo, 1700, 1800, 1900...
"""
"""
print('\n*** DESCOBRINDO QUAL ANO FOI OU SERÁ BISSEXTO ***')
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} NÃO é bissexto!'.format(ano))
print('-=' * 15)
"""

print('\n*** DESCOBRINDO QUAL ANO FOI OU SERÁ BISSEXTO ***')
from datetime import date # função que pega o ano atual do computador
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year #  Essa linha de comando pega o ano atual do computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} NÃO é bissexto!'.format(ano))
print('-=' * 15)
