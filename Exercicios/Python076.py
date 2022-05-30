'''
Crie um programa que tenha uma tupla única com nome de produto e seus
respectivos preços na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
'''

prod_valor = 'Leite, 4.95', 'Arroz, 21.00', 'Feijão, 7.75', 'Macarrão, 2.85', 'Biscoito, 1.75', 'Café, 17.50', 'Açucar, 2.99', 'Farinha, 4.80'
print('-' * 30)
print(f'{"LISTA DE ITENS":^30}')
print('-' * 30)
for itens in range(0, len(prod_valor)):
    if itens % 2 == 0: # Todos itens estão em uma posição par (0=Leite, 2=Arroz etc)
        print(f'{prod_valor[itens]:.<30}', end='')
    else:
        print(f'R${prod_valor}')
print('-' * 30)
