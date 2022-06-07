
votos_bolsonaro = 0
votos_lula = 0
while True:
    print('''Qual é sua intenção de voto?
        [ 1 ] - Bolsonaro
        [ 2 ] - Lula''')
    voto = int(input('Digite uma opção de candidato:' ))
    print(f'TOTAL BOLSONARO: {votos_bolsonaro}')
    print(f'TOTAL LULA: {votos_lula}')
    if voto == 1:
        votos_bolsonaro += 1
    elif voto == 2:
        votos_lula += 1
    else:
        print('Opção iválida. Tente novamente!')
