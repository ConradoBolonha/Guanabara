"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule
a sua área e quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta
pinta uma área de 2mº
"""
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite  altura da parede: '))
area = float(largura*altura)
tinta = float(area/2)
print('Serão necessários {} litros de tintas para pintar {:.2f}m²'.format(tinta, area))
