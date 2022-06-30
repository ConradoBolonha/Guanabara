'''
Crie um programa que leia vários números e coloque em uma lista. Depois disso mostre:

a) Quantos números foram digitados;
b) A lista de valores ordenada de forma decrescente;
c) Se o valor 5 foi digitado e se está ou não na lista.
'''

numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'nN':
        break
print(f'Foram digitados {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'Os números em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
