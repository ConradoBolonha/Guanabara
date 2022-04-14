"""
Desenvolva um programa que pergunte a distância de uma viagem em
quilômetros, calcule o preço da passagem, cobrando R$ 0,50 por
quilômetro para viagens de até 200Km e R$ 0,45 para viagens mais longas.
"""

dist = int(input('\nDigite a distância da sua viagem: '))
acima_200 = float(dist * 0.45)
ate_200 = float(dist * 0.50)
if dist >= 200:
    print('O valor da viagem é de R$ {:.2f}'.format(acima_200))
else:
    print('O valor da viagem é de R$ {:.2f}'.format(ate_200))
