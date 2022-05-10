"""
Crie um programa que leia um frase qualquer e diga se ela
é um palíndromo, desconsiderando os espaços.
"""

palin = str(input('\nDigite uma palavra: ')).strip().upper()
palavra = palin.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('A frase invertida é {}'.format(inverso))
if inverso == junto:
    print('TEMOS um palíndromo!')
else:
    print ('NÃO temos um palíndromo!')

#  OU

"""
palin = str(input('\nDigite uma palavra: ')).strip().upper()
palavra = palin.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso da frase {} é {}'.format(junto, inverso))
if inverso == junto:
    print('TEMOS um palíndromo!')
else:
    print ('NÃO temos um palíndromo!')
"""
