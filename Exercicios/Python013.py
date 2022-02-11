
"""
Faça um algoritmo que leia um salário de um funcionário e
depois, mostre seu novo salário com 15% de aumento.
"""

sal = float(input('Digite o valor do salário: R$ '))
aumento = sal*0.15
sal_reajuste = sal+aumento
print('O salário será reajustado para R$ {:.2f}'.format(sal_reajuste))
