
valores = list()
for cont in range(0 , 5):
    valores.append(int(input('Digite um valor: ')))

for cont, val in enumerate(valores):
    print(f'Na posição {cont} encontrei os valores {val}')
print('FIM')
