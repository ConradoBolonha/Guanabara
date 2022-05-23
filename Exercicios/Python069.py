'''
Crie um programa que leia o sexo e idade de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer
ou não continuar. No final mostre:

a) Quantos pessoas tem mais de 18 anos;
b) Quantos homens foram cadastrados;
c) Quantos mulheres tem menos de 20 anos.
'''

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    mais18 = 0
    homens = 0
    mulher18 = 0
    while sexo not in 'MF': # "MF" = Masculino ou Feminino
        sexo = str(input('Sexo [M/F]: ')).strip().upper() [0]
        
    resposta = ' '
    while resposta not in 'SN': # "SN" = Sim ou Não
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    if resposta == 'N':
        break
print('FIM')
