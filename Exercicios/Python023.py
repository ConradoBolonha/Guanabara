"""
Faça um programa que crie um número de 0 a 9999 e
mostre na tela cada um dos digitos separados.
Ex: Número 1529
unidade: 9
dezena: 2
centena: 5
milhar: 1

Obs: Tente fazer como String e matematicamente
"""

milhar = input('Digite um número milhar: ')
print('Unidade: {}'.format(milhar[3]))
print('Dezena: {}'.format(milhar[2]))
print('Centena: {}'.format(milhar[1]))
print('Milhar: {}'.format(milhar[0]))
