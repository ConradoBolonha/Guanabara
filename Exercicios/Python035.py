"""
Desenvolva um algoritmo que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.
"""
print('\n')
print('-=' * 17)
print(' *** ANALISADOR DE TRIÂNGULOS ***')
print('-=' * 17)
r1 = float(input('Tamanho do primeiro segmento: '))
r2 = float(input('Tamanho do segundo segmento: '))
r3 = float(input('Tamanho do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima FORMAM um triângulo!')
else:
    print('Os segementos acima NÃO FORMAM um triângulo!!!')
