print('\nCALCULANDO MÉDIA ESCOLAR')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7.0:
    print('Sua média é \033[32m{:.1f}\033[m. Parabéns, foi aprovado!'.format(media))
else:
    print('Hummm, sua média foi \033[31m{:.1f}\033[m e NÃO passou. Refaça a avaliaçao!'.format(media))
print('\033[0;35;42m**** NUNCA PARE DE ESTUDAR!!! ****\033[m')
