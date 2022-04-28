print('=-' * 5, 'CONVERSOR DE HORAS, MINUTOS E SEGUNDOS', '=-' * 5)
print('''\nEscolha uma opção para ver sua conversão:
[ 1 ] - HORAS em MINUTOS
[ 2 ] - HORAS em SEGUNDOS
[ 3 ] - MINUTOS em SEGUNDOS''')
opcao = int(input('\nDigite uma das opções de conversão: '))
if opcao == 1:
    horas = int(input('Digite a quantidade de HORAS: '))
    horas_minutos = 60 * horas    
    print('\nNa conversão de {} hora(s), temos {} minutos.'.format(horas, horas_minutos))
elif opcao == 2:
    horas = int(input('Digite a quantidade de HORAS: '))
    horas_segundos = 3600 * horas
    print('\nNa conversão de {} hora(s), temos {} segundos.'.format(horas, horas_segundos))
elif opcao == 3:
    minutos = int(input('Digite a quantidade de MINUTOS: '))
    minutos_segundos = minutos * 60
    print('\nNa conversão de {} minutos, temos {} segundos.'.format(minutos, minutos_segundos))
