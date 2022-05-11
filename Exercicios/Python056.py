"""
Leia um programa que leia o nome, idade e sexo de 4 pessoas
e que no final o programa mostre:

* A média de idade do grupo;
* Qual é o nome homem mais velho;
* Quantos mulheres tem menos de 21 anos.
"""

SomaIdade = 0
MediaIdade = 0
MaiorIdadeHomem = 0
NomeVelho = ''
TotalMulher20 = 0
for pessoa in range(1, 5):
    print('\n{}ª pessoa: '.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    SomaIdade += idade
    if pessoa == 1 and sexo in 'Mn':
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo in 'Mn' and idade > MaiorIdadeHomem:
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        TotalMulher20 += 1
MediaIdade = SomaIdade / 4
print('A média de idade do grupo é de {} anos.'.format(MediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(MaiorIdadeHomem, NomeVelho))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(TotalMulher20))
