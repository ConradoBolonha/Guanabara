'''
Crie um algoritmo que leia o sexo de uma pessoa que só aceite "F" e "M".
Caso esteja errado, peça a digitação novamente até que digite o valor
correto.
'''

sexo = str(input('Digite o sexo [M / F]:')).upper()
while sexo == 'M' and sexo == 'F':
    print str(input('Sexo inválido! Tente novamente: ')
