"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

1-O nome completo com todas as letras maiúscula;
2-O nome com todas minúsculas;
3-Quantas letras ao todo (sem considerar espaços);
4-Quantas letras tem o primeiro nome.
"""
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
# dividido = nome.split()
print('Convertendo seu nome em maiúsculo: {}'.format(nome.upper()))
print('Convertendo seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem {} caracteres'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} caracteres'.format(len(dividido[0])))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))
