"""
Crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira.
"""
#  import math
#  num = float(input('Digite um valor: '))
#  print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, math.trunc(num)))
#  print('O valor digitado foi {} e seu arredondamento para cima é {}.'.format(num, math.ceil(num)))
#  print('O valor digitado foi {} e seu arredondamento para baixo é {}.'.format(num, math.floor(num)))

#  from math import trunc
#  num = float(input('Digite um número: '))
#  print(' O valor digitado é {} e sua porção inteira é {}'.format(num, trunc(num)))

num = float(input('Digite um número: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
