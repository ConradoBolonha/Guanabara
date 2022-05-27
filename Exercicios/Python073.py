'''
Crie uma tupla preenchiada  com os 20 primeiros colocados da tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação e depois
mostre:

a) Os 5 primeiros;
b) Os últimos 4 colocados;
c) Times em ordem alfabética;
d) Em que posição está o time da Chapecoense.
'''

times = 'Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta' ,'Atlético-GO'

print(f'A) Os cinco primeiros times são {times[0:6]}')
print(f'B) Os quatro últimos são {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na posição {times.index("Chapecoense") + 1}.')
