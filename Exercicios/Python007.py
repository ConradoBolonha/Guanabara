
# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2) / 2
print('A média é: {} '.format(media))
if media < 7.0:
    print('Você NÃO atingiu a média.')
else:
    print('Parabéns, passou de ano!')
