"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

1-O nome completo com todas as letras maiúscula;
2-O nome com todas minúsculas;
3-Quantas letras ao todo (sem considerar espaços);
4-Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome: '))
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
