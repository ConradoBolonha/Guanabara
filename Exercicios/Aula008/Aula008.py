"""
bebida = suco, água, refrigerante
doces = pudim, bolo, sorvete
comida = lanche, pizza, sopa

# >>> import bebida
# >>> import doce

# >>> from doce import pudim
"""

import math
num = int(input('Digite um número: '))
result = int(math.sqrt(num))
print('A raiz quadrada de {} é {}'.format(num, result))
