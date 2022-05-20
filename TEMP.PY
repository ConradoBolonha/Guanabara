numero = 0
soma = 0
contador = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    contador = contador + 1
    soma = soma + numero
#  print('Você digitou {} números e soma é {}.'.format(contador, soma))
print(f'Você digitou {contador} números e a soma é {soma}.')
