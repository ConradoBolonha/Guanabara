"""
Um professor que sortear um dos seus quatro alunos para apagar
o quadro. Faça um algoritmo que ajude ele, lendo nome deles e
escrevendo na tela o nome do aluno sorteado.
"""

#  import random
#  nome_1 = str(input('Digite o nome do primeiro aluno: '))
#  nome_2 = str(input('Digite o nome do segundo aluno: '))
#  nome_3 = str(input('Digite o nome do terceiro aluno: '))
#  nome_4 = str(input('Digite o nome do quarto aluno: '))
#  lista = [nome_1, nome_2, nome_3, nome_4]
#  escolhido = random.choice(lista)
#  print('O aluno escolhido foi {}'.format(escolhido))

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = (choice(lista))
print('O escolhido foi {}'.format(escolhido))
