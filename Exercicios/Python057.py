'''
Crie um algoritmo que leia o sexo de uma pessoa que só aceite "F" e "M".
Caso esteja errado, peça a digitação novamente até que digite o valor
correto.
'''

sexo = str(input('Digite o sexo [M / F]: ')).strip().upper() [0] # [0] só pega a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido. Informe o sexo corretamente: ')).strip().upper() [0]
print('Sexo {} registrado com sucesso!'.format(sexo))
