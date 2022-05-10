"""'
Desenvolva um programa que leia o primeiro termo e razão
de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos
dessa progressão.
"""

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
prim_termo = int(input('Primeiro termo: ')) #  Número pelo qual se dará o início da contagem
razao = int(input('Razão: ')) # Se razão = 5, irá pular de 5 em 5 por exemplo.
decimo_termo = prim_termo + (10 - 1) * razao
for cont in range(prim_termo, decimo_termo + razao, razao):
    print('{} '.format(cont), end = ' -> ')
print('FIM')
