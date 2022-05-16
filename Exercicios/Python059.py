'''
Crie um algoritmo que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplcar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

valor1 = int(input('\nDigite um valor inteiro: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplcar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')
    opcao = int(input('>>>>>> Escolha uma opção: '))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é {}.'.format(valor1, valor2, soma))
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print('A subtração entre {} e {} é {}.'.format(valor1, valor2, multiplicacao))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
    elif opcao == 4:
        print = ('Digite novamente: ')
        valor1 = int(input('Digite um valor inteiro: '))
        valor2 = int(input('Digite o segindo valor: '))
    elif opcao == 5:
        print('Programa encerrado!')
    else:
        print('Opção inválida: Digite novamente!')
print('\n*** FIM ***')
