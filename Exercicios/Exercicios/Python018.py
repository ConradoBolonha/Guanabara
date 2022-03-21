"""
Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# import math
# an = float(input('Digite o ângulo: '))
# se = math.sin(math.radians(an))
# co = math.cos(math.radians(an))
# ta = math.tan(math.radians(an))
# print('O valor do seno é {:.2f}, cosseno é {:.2f} e a tangente {:.2f}'.format(se, co, ta))

#  from math import radians, sin, cos, tan
#  an = float(input('Digite o ângulo: '))
#  se = sin(radians(an))
#  print('O ângulo de {} tem um seno de {:.2f}'.format(an, se))
#  co = cos(radians(an))
#  print('O ângulo de {} tem um cosseno de {:.2f}'.format(an, co))
#  ta = tan(radians(an))
#  print('O ângulo de {} tem uma tangente de {:.2f}'.format(an, ta))

import math
an = float(input('Digite o ângulo: '))
se = math.sin(math.radians(an))
print('O ângulo de {} tem um seno de {:.2f}'.format(an, se))
co = math.cos(math.radians(an))
print('O ângulo de {} tem um cosseno de {:.2f}'.format(an, co))
ta = math.tan(math.radians(an))
print('O ângulo de {} tem uma tangente de {:.2f}'.format(an, ta))
