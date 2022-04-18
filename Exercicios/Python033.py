"""
Faça um programa que leia três números e mostre qual é o
maior e qual é o menor.
"""

print('\n*** DIGITE TRÊS NÚMEROS PARA VER QUAL É O MENOR E O MAIOR VALOR DIGITADO ***')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))
#  VERIFICANDO QUEM É O MENOR:
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# VERIFICANDO QUEM É O MAIOR:
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O número menor é {} e o maior é {}.'.format (menor, maior))
