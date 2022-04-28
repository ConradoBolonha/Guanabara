"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

* À vista: dinheiro/cheque: 10% de desconto.
* À vista no cartão de débito: 5% de desconto.
* Em até duas vezes no cartão de crédito: preço normal.
* Três vezes ou mais no cartão de crédito: 20% de juros.
"""

print('{:=^40}'.format(' LOJAS TEM TUDO '))
vl_prod = float(input('\nDigite o valor do produto: R$ '))
print('''\nFORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] Á vista no cartão de débito
[ 3 ] 2X no crédito
[ 4 ] 3X ou mais no crédito\n''')
fpag = int(input('Digite a forma de pagamento: '''))
if fpag == 1:
    vl_total = vl_prod - (vl_prod * 10 / 100)
elif fpag == 2:
    vl_total = vl_prod - (vl_prod * 5 /100)
elif fpag == 3:
    vl_total = vl_prod
elif fpag == 4:
    vl_total = vl_prod + (vl_prod * 20 / 100)
print('O produto custa {:.2f} e o valor da compra será de R$ {:.2f}'.format(vl_prod, vl_total))
