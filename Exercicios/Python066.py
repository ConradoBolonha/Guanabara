'''
Crie um algoritmo que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar 999, que é 
a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles desconsiderando a flag de parada (999)
'''
numero = 0
soma = 0
contador = 0
while True:
    numero = int(input('Digite um número (ou 999 para parar): '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Você digitou {contador} números e a soma entre eles é {soma}.')
