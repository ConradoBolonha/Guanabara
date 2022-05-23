'''
Faça um programa que mostre a tabuada de vários números um de cada
vez. Para cada valor digitado pelo usuário, o programa será
interrompido quando o número solicitado for negativo.
'''

print('\n','-=' * 8, ' TABUADA ', '-=' * 8, '\n')
contador = 0
while True:
    numero = int(input('\nDigite um numero para ver sua tabuada: '))
    if numero < 0:
        break
    for contador in range(1, 11):
        print(f'{numero} X {contador} = {numero * contador}')
    print('#-' * 10)
print('Obrigado, até logo!')
