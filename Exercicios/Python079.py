'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
será adicionado. No final, serão exibidos todos os valores únicos digitados
em ordem crescente.
'''

numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print('Valor já inserido. Informe outro!')
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'nN':
        break
numeros.sort()
print(f'Os números digitados foram {numeros}.')
