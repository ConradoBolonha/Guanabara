"""
Crie um algoritmo que leia uma frase pelo teclado e mostre:

1-Quantas vezes aparece a letra "A";
2-Em que posição ela aparece a primeira vez;
3-Em que posição ela aparece a última vez.
"""

frase = 'Amanhã, com certeza irá chover'
print(frase)
print('Na string, contém {} letra "A".'.format(frase.count('A')))
print('A letra "A" está na posição {}.'.format(frase.find('A')))
print('A letra "A" aparece em mais alguma posição? {}'.format('A' in frase[1::]))
