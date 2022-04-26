"""
Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:

1 para binário;
2 para octal;
3 para hexadecimal
"""

num = int(input('\nDigite um número para saber sua conversão: '))
print('''\nEscolha uma opção de conversão:
[ 1 ] Converter para binário
[ 2 ] Converter pata octal
[ 3 ] Converter para hexadecimal''')
opcao = int(input('\nDigite sua opção: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}.'.format(num, bin(num)[2:])) #  [2:] -> Exclui as duas primeiras casas
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format (num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!!!')
