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

idade = int(input('\nDigite a idade do atleta: '))
if idade <= 9:
    print('Categoria: MIRIM') 
elif idade >= 10 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Categoria: JUNIOR')
elif idade == 20:
    print('Categoria: SÊNIOR')
elif idade >= 21:
    print('Categoria: MASTER')
