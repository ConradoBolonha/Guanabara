"""
Crie um algoritmo que leia uma frase pelo teclado e mostre:

1-Quantas vezes aparece a letra "A";
2-Em que posição ela aparece a primeira vez;
3-Em que posição ela aparece a última vez.
"""

frase = (         'Amanhã, com certeza irA chover'         ).strip()
print(frase)
print('Na string, contém {} letra "A".'.format(frase.count('A')))
print('A primeira letra "A" está na posição {}.'.format(frase.find('A') + 1))
print('Em que posição a letra "A" aparece a última vez? {}'.format(frase.rfind('A') + 1))
