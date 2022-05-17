'''
Refaça o desafio 051 lendo o primeiro termo e a razão de uma PA (progressão aritimética),
mostrando os 10 primeiro termos da progressão usando a estrutura while.
'''

print('\n','-=' * 8, 'GERADOR DE TERMO', '=-' * 10)
primeiro_termo = int(input('\nDigite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end = '')
    termo = termo + razao
    contador = contador+ 1
print('FIM', '\n')
