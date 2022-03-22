"""
Crie um algoritimo que sorteie a ordem de apresentação de trabalho dos alunos, leia o nome dos quatro alunos
e mostre a ordem de sorteio
"""
from random import shuffle
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de sorteio ficou:\n', lista)
