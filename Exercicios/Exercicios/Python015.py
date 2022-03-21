"""
Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por
quilômetro rodado.
"""

dias_alu = int(input('Quantos dias alugado? '))
km_rod = float(input('Quantos quilômetros rodados? '))
val_dia = 60.00
val_quil = 0.15
tot_pagar = (dias_alu * val_dia) + (km_rod * val_quil)
print('O total a pagar é de R$ {:.2f}'.format(tot_pagar))
