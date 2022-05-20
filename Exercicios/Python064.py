'''
Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar 999, sendo esta a
condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag 999).
'''
num = 0         #  --\
contador = 0    #  ---| ==> ou juntar todas variáveis: num = contador = soma = 0
soma = 0        #  --/
num = int(input('Digite um número qualquer ou 999 para parar: ')) # Duplicando essa linha, irá desconsiderar 999 na soma
while num != 999:
    soma += num  #  OU soma = soma + num
    contador += 1  #  OU contador = contador + 1
    num = int(input('Digite um número qualquer ou 999 para parar: ')) #  # Duplicando essa linha, irá desconsiderar 999 na soma
print('Você digitou {} números e soma entre eles é {}.'.format(contador, soma))
print('*** FIM ***')
