
#  -----------------------------------------------------------------------
#  ------------------ ESTRUTURAS ANINHADAS    ----------------------------
#  -----------------------------------------------------------------------

####  ESTRUTURA CONDICIONAL SIMPLES (porque só tem uma condição ("if"))  ####
nome = str(input('Digite seu nome: '))
if nome == 'Conrado':
    print('Olá Sr. {}'.format(nome))
print('Tenha um bom dia!!!')

####  ESTRUTURA CONDICIONAL COMPOSTA  (porque tem duas condições ou mais ("if" e "else")  ####
nome2 = str(input('Digite seu nome: '))
if nome2 == 'Conrado':
    print('Sim, seu nome é {}'.format(nome2))
else:
    print('Olá {}, como tem passado?'.format(nome2))
print('Tenha um bom dia!!!')

####  OUTRO EXEMPLO DE ESTRUTURA CONDICIONAL COMPOSTA  ####
nome3 = str(input('Digite seu nome: '))
if nome3 == 'Conrado':
    print('Seu nome é bonito Sr. {}!'.format(nome3))
elif nome3 == 'Ana' or nome3 == 'Maria' or nome3 == 'Pedro':
    print('{}, seu nome é tão normal!'.format(nome3))
else:
    print('Tenha uma boa tarde!')
