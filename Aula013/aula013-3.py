inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for cont in range(inicio, fim + 1, passo):
    print(cont)
print(' FIM ')

"""'
Se inicio = 1, fim = 30 e passo = 5
O resultado será de 1 a 30 pulando de 5 em 5 números.
"""