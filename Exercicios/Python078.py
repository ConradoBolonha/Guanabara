'''
Faça um programa que leia 5 valores númericos e guarde em uma lista. No final,
mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.

'''

listanum = []
maior = 0
menor = 0
for cont in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = listanum[cont]
    else:
        if listanum[cont] > maior:
            maior = listanum[cont]
        if listanum[cont] < menor:
            menor = listanum[cont]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f'{indice}.', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}.', end='')
