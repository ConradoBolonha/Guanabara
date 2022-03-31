"""
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente.

"""
nome = input('Digite o seu nome completo: ')
div_nome = nome.split()
print(div_nome[0:])