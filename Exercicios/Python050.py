"""
Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for
ímpar, desconsidere-o.
"""
soma = 0
contad = 0
for cont in range(1, 7):
    num = int(input('Digite o {}º número: '.format(cont)))
    if num % 2 ==0:
        soma += num #  ou "soma = soma + num"
        contad += 1 # ou "contad = contad + 1"
print('Você informou {} números pares é a soma entre eles é {}.'.format(contad, soma))
