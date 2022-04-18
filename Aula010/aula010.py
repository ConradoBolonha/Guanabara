"""
Clie um algoritimo que analise o ano do seu carro e
se for abaixo do ano digitado, mostre uma mensagem, se não,
mostre outra mensagem
"""

ano_carro = int(input('Digite o ano do seu carro: '))
if ano_carro <= 2010:
    print ('Seu carro está velinho!')
else:
    print('Seu carro é novo!!!')
print('-- FIM --')

"""
# Algoritmo simplificado (NÃO É MUITO UTILIZADO. DIFICULTURA A LEITURA):
ano_carro = int(input('Digite o ano do seu carro: '))
print('Carro está velinho!' if ano_carro <= 2010 else 'Seu carro é novo! ')
print('** FIM **')
"""
