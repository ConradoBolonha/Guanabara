"""
Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$ 1.200,00, calcule um aumento de 10%.
para os inferiores ou iguais, o aumento é de 15%.
"""

sal = float(input('\nDigite o valor do salário: '))
if sal >= 1200.00:
    print('O salário será de R$ {:.2f}'.format(sal * 0.10 + sal))
else:
    print('O salário será de R$ {:.2f}'.format(sal * 0.15 + sal))
