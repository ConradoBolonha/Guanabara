"""
Crie um programa que leia um número inteiro e mostre na tela se
ele é PAR ou ÍMPAR.
"""

num = int(input('Digite um número: '))
#  p_i = num + 2
p_i = num % 2
if p_i == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
