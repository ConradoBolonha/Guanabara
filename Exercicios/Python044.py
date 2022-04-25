"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

* À vista: dinheiro/cheque: 10% de desconto.
* À vista no cartão de débito: 5% de desconto.
* Em até duas vezes no cartão de crédito: preço normal.
* Três vezes ou mais no cartão de crédito: 20% de juros.
"""

vl_prod = float(input('Digite o valor do produto: '))
av_dc = vl_prod - vl_prod * 0.10
av_deb = vl_prod - vl_prod * 0.05
div_2x = vl_prod
div_3x = vl_prod + vl_prod * 0.20
#  print(av_dc, av_deb, div_2x, div_3x)
if 