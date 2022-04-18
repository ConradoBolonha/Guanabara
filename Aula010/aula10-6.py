#  ALGORITIMO PARA CALCULAR A MÉDIA DAS NOTAS ESCOLARES

print ('\n=== Digite ambas notas para calcular sua média ===')
nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('Sua media foi {:.2f}. Parabéns, você atingiu a média e passou de ano! :-)'.format(media))
else:
    print('Sua média foi {:.2f} e você NÃO atingiu a média mínina 7.0. Estude mais!'.format(media))
