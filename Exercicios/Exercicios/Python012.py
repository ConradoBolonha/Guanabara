
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

val_prod = float(input('Digite o valor do produto: '))
desc = val_prod * 0.05
val_final = val_prod-desc
print('Se comprar a vista, o valor final é {:.2f}'.format(val_final))
