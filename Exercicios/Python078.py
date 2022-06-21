'''
Faça um programa que leia 5 valores númericos e guarde em uma lista. No final,
mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.
'''

val_num = []
val_maior = 0
val_menor = 0
for val_pos in range(0, 5):
    val_num.append(int(input(f'Digite um valor na posição {val_pos}: ')))
    if val_pos == 0:
        val_maior = val_menor = val_num(val_pos)
    else:
        if val_num[val_pos] > val_maior:
            val_maior = val_num[val_pos]
        if val_num[val_pos] < val_menor:
            val_menor = val_num(val_pos)
print(f'Você digitou os valores {val_num}')
print(f'O maior valor digitado foi {val_maior} na posição ')
for indice, valor in enumerate(val_num):
    if valor == val_maior:
        print(f'{indice}...', end='')
print(f'O menor valor digitado foi {val_menor} na posição ')
for indice, valor in enumerate(val_num):
    if valor == val_menor:
        print(f'{indice}...', end='')
