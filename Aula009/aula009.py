
#  Fatiamento de String

frase = 'Curso em Vídeo Python'
print(frase[9:14])

frase2 = 'Teste fatiamento de string'
print(frase2[6:16])

# Fatiamento de String com salto
frase3 = 'Frase do dia com salto de dois em dois'
print(frase3[0:41:2])

frase4 = 'Frase do dia com salto de três em três'
print(frase4)
print(len(frase4))
print(frase4[0:38:3])

# Análise de uma string
# len = conta a quantidade de caracter
frase5 = 'Frase do dia usando a função "count"'
print (len(frase5))

# count = Contas quantas letras "e" a frase tem.
frase6 = 'Meus estudo em Python'
print(frase6.count('e'))

# Conta a quantidade da letra "e" do caracter 0 ao 13.
frase7 = 'Meu estudo em Python vai que vai'
print(frase7.count('e', 0, 10))

# find = Mostra a posição de um caracter
frase8 = 'Localizador de letras usando o argumento find'
print(frase8.find('tras'))

# comando "in" -> Procura caracter(s) e mostra True ou False.
frase9 = 'Procurando caracter(s) com o comando "in"'
print('com')