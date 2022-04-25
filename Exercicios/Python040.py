"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final de acordo coma  média atingida:

* Média abaixo de 4.9: REPROVADO
* Média entre 5.0 e 6.9: RECUPERAÇÃO
* Média 7.0 ou superior: APROVADO

"""

n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 4.9:
    print('Sua média é {} e portanto, foi REPROVADO!'.format(media))
elif media > 5.0 and media < 6.9:
    print('Sua média {} deixou você de RECUPERAÇÃO!'.format(media))
elif media > 7.0:
    print('Sua média foi {}. Parabéns, foi APROVADO!'.format(media))
