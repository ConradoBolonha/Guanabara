'''
Crie um programa que leia vários números e coloque em uma lista. Depois, crie
duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'nN':
        break
for indice, valor in enumerate(numeros):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print(f'Os números digitados são {numeros}')
print(f'Os números pares são {pares} e os ímpares são {impares}')
