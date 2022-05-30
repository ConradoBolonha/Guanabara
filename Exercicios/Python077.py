'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois, disso, deve mostrar para cada palavra, quais são as suas vogais.
'''

palavras = 'notebook', 'teclado', 'programador', 'python', 'aprendendo', 'chuva', 'copiadora', 'analista', 'sistema'
for pal in palavras:
    print(f'\nNa palavra {pal.upper()} temos ', end='')
    for letra in pal:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
