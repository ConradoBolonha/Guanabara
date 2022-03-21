n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('Sua média é {}'.format(media))
if media >= 7.0:
    print('Parabéns. Você passou!')
else:
    print('Não atingiu a média. Estude mais.')
