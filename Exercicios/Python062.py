'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais algum termo. O
programa encerra quando ele disser que quer mostrar 0 termos.
'''

print('\n','-=' * 8, 'GERADOR DE TERMO', '=-' * 10)
primeiro_termo = int(input('\nDigite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
contador = 1
total = 0
novos_termos = 10
while novos_termos != 0:
    total = total + novos_termos
    while contador <= total:
        print('{} -> '.format(termo), end = '')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA', '\n')
    novos_termos = int(input('Quantos termos a mais deseja mostrar? '))
print('\nA progressão executada mostrou {} termos.'.format(total))
print('*** FIM ***')
