'''
Desenvolva um programa que leia quatro valores pelo teclado,
guarde-os em uma tupla e que no final mostre:

a) Quantas vezes apareceu o valor 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.
'''

numero = int(input('Digite um número: ')), int(input('Digite um 2º número: ')), int(input('Digite um 3º número: ')), int(input('Digite um 4º número: '))
print(f'O valor 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'A primeira posição do número 3 foi a {numero.index(3) + 1}')
else:
    print('O valor 3 não foi digitado.')
print(f'Os número pares são ', end='')
for num_par in numero:
    if num_par % 2 == 0:
        print(num_par, end =' ')
