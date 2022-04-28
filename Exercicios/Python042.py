"""
Refaça o desafio 35 dos triângulo, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

* Equilátero: Todos os lados são iguais.
* Escaleno: Todos os lados são diferentes.
* Isóceles: Dois lados iguais.
"""

r1 = float(input('\nTamanho do primeiro segmento: '))
r2 = float(input('Tamanho do segundo segmento: '))
r3 = float(input('Tamanho do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima FORMAM um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo formado é um EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado é um ESCALENO')
    else:
        print('O triângulo formado é um ISÓCELES.')
else:
    print('O valores digitados não formam um triângulo.')