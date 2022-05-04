
###  CONDIÇÃO SIMPLES: Tem somente o "if".
"""
nome = str(input('\nQual é seu nome? '))
if nome == 'Conrado':
    print ('Sim {}, esse é seu nome!'.format(nome))
print('Tenha um bom dia {}!!!'.format(nome))
#________________________________________________________________________
### CONDIÇÃO COMPOSTA: Tem o "if" e o "else".

sobrenome = str(input('\nQual seu último sobrenome? '))
if sobrenome == 'Bolonha':
    print('Olá Sr. {}, prazer!!!'.format(sobrenome))
else:
    print('Sr. {}, essa é uma condição composta!'.format(sobrenome))
print('Tenha uma ótima tarde Sr. {}'.format(sobrenome))
#________________________________________________________________________
### CONDIÇÃO ANINHADA: Tem a condição "elif".

nome_com = str(input('Digite alguns nomes normais: '))
if nome_com == 'Daniel':
    print('Olá Sr. {}!'.format(nome_com))
elif nome_com == 'João' or nome_com == 'Maria' or nome_com == 'José':
    print('{}, seu nome é tão normal!'.format(nome_com))
else:
    print('Sr. {}, a condição ELSE foi ativada!'.format(nome_com))
"""
#________________________________________________________________________
### CONDIÇÃO ANINHADA COM MAIS DE UM "elif".

name = (str(input('\nDigite seu nome: ')))
if name == 'Conrado':
    print('Olá Sr, {}!'.format(name))
elif name == 'João' or name == 'Maria':
    print('Seu nome é tão normal {}'.format(name))
elif name in ('Solange Eduarda Beatriz Edna'):
    print('Seu nome está listado na condição "in"!')
else:
    print('Sr. {}, a condição "else" foi ativada.'.format(name))
