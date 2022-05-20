'''
Crie um programa que leia vários números inteiros pelo teclado e que no
final da execução, mostre a média entre todos os valores e qual foi
o maior e menor valores lidos. O programa deve perguntar para o
usuário se ele quer ou não continuar a digitar valores.
'''

resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quantidade
print('Você digitou {} números e a média foi {:.0f}.'.format(quantidade, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
print('*** FIM ***')
