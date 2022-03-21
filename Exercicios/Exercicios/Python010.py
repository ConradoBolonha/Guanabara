
# Crie um programa para uma pessoa que converta o dinheiro que ela tem na carteira em dólar.

real = float(input('Digite um valor em real: R$ '))
dolar = real/5.22
euro = real/6.11
print('Com R$ {:.2f} você pode comprar US${:.2f} ou €{:.2f} '.format(real, dolar, euro))
