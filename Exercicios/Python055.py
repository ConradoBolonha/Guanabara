"""'
Faça um programa que leia o peso de cinco pessoas e mostre no
final, qual foi o maior e menor peso lidos.
"""
maior_peso = 0
menor_peso = 0
for pessoas in range(1, 6):
    peso = float(input('\nPeso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso é de {} e o menor é {}'.format(maior_peso, menor_peso))
