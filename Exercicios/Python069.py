'''
Crie um programa que leia o sexo e idade de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer
ou não continuar. No final mostre:

a) Quantos pessoas tem mais de 18 anos;
b) Quantos homens foram cadastrados;
c) Quantos mulheres tem menos de 20 anos.
'''

mais18 = 0
total_homens = 0
fem20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': # "MF" = Masculino ou Feminino
        sexo = str(input('Sexo [M/F]: ')).strip().upper() [0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:        
        fem20 += 1        
    resposta = ' '
    while resposta not in 'SN': # "SN" = Sim ou Não
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    if resposta == 'N':
        break
print(f'{mais18} pessoas tem mais de 18 anos.')
print(f'{total_homens} homens foram cadastrados.')
print(f'{fem20} mulheres tem menos de 20 anos.')
