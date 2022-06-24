'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista JÁ NA POSIÇÃO correta de inserção
sem usar o comando "sort()". No final, mostre a lista ordenada na tela. 
'''

valores = []
for cont in range(0, 5):
    numero = int(input('Digite um valor: '))
    if cont == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        posicao = 0
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                break
            posicao += 1
print(f'Os valores ordenados são {valores}')
