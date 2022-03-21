
# Faça um programa que calcule Celsius para Fahrenheit ou Fahrenheit para Celsius.
# Fahrenheit = C x 1.8 + 32
# Celsius = F - 32 / 1.8

cel = float(input('Digite a temperatura em Celsius: '))
fah = float(input('Digite a temperatura em Fahrenheit: '))
temp_fah = cel * 1.8 + 32
temp_cel = (fah - 32) / 2
print('A temperatura em Fahrenheit é {:.1f}ºF e em Celsius, a temperatura é {:.1f}ºC'.format(temp_fah, temp_cel))
