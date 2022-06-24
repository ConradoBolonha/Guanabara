'''
Crie um programa que leia vários números e coloque em uma lista. Depois disso mostre:

a) Quantos números foram digitados;
b) A lista de valores ordenada de forma decrescente;
c) Se o valor 5 foi digitado e se está ou não na lista.
'''

numeros = []
contagem = 0
while True:
    valores = int(input('Digite um valor: '))
    if valores not in numeros:
        numeros.append(valores)
    else:
        print('Valor já digitado. Escolha outro! ')
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'nN':
        break
print(f'Foram digitados {contagem} números.')
print(f'Os numeros em ordem decrescente são {numeros.reverse}')
print(f'O valor ')