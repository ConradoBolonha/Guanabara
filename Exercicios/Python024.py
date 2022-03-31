"""'
Crie um programa que lei o nome de uma cidade e diga
se ela começa ou não com o nome "Santo"
"""

cidade = input('Digite o nome de uma cidade: ')
div_cidade = (cidade.split())
print('Santo' in div_cidade[0])
