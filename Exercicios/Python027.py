"""
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.
"""

nome = str(input('Digite o seu nome completo: ')).strip()
div_nome = nome.split()
print(div_nome[0])
print(div_nome[len(div_nome)-1])
