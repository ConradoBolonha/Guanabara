"""
Faça um programa que calcule a soma entre todos os números
ímpares que são múltiplos de 3 e que se encontram no
intervalo de 1 até 500.
"""

soma = 0
contad = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        contad = contad + 1 #  ou contad += 1
        soma = soma + cont
print('A soma de todos os {} números é {}'.format(contad, soma))
