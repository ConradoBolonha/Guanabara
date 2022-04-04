"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

1-O nome completo com todas as letras maiúscula;
2-O nome com todas minúsculas;
3-Quantas letras ao todo (sem considerar espaços);
4-Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome: ')).strip()
#  dividir = nome.split()
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome completo tem {}'.format(len(nome) - nome.count(' ')))
#  print('Seu primeiro nome tem {}'.format(len(dividir[0])))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))
