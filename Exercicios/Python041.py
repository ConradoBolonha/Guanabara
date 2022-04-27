"""
A Confederação Nacioanal de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua 
categoria de acordo com a idade:

* Até 9 anos: MIRIM
* De 10 a 14 anos: INFANTIL
* De 15 a 19 anos: JUNIOR
* Com 20 anos: SÊNIOR
* Acima de 21 anos: MASTER
"""
from datetime import date

ano = int(input('\nDigite o ano de nascimento do atleta: '))
data = date.today().year
idade = data - ano
if idade <= 9:
    print('O atleta tem {} anos e sua categoria é MIRIM.'.format(idade)) 
elif idade >= 10 and idade <= 14:
    print('O atleta tem {} anos e sua categoria é INFANTIL.'.format(idade))
elif idade >= 15 and idade <= 19:
    print('O atleta tem {} anos e sua categoria: JUNIOR.'.format(idade))
elif idade == 20:
    print('O atleta tem {} anos e sua categoria é SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e sua categoria é MASTER.'.format(idade))
