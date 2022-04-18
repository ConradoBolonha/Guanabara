"""'
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80Km/h, mostre uma mensagem dizendo que ele foi multado e a multa acresce
R$ 7,00 por cada Km acima do limite.
"""
"""
vel = float(input('\nDigite a velocidade: '))
vl_multa = (vel - 80) * 7
if vel > 80:
    print('O limite de 80Km/h foi atingido. Sua multa será de R$ {:.2f}'.format(vl_multa))
else:
    print('Use sempre o cinto de segurança! Boa viagem!!!')
"""

vel = float(input('Digite a velocidade: '))
vl_multa = (vel - 80 ) * 7
if vel > 80:
    print('Você foi multado. A multa será de R$ {:.2f}'.format(vl_multa))
print('Diriga com segurança. Tenha uma boa viagem!!!')
