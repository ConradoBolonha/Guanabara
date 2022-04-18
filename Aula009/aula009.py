
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

# Comando "in" -> Procura caracter(s) e mostra True ou False.
frase9 = 'Procurando caracter(s) com o comando "in"'
print('comando' in frase9)

# Comando "replace" -> Troca(reposiciona) uma frase na string
frase10 = 'Usando o comando "replace" para reposicionar uma frase'
print(frase10.replace('comando','command'))

# Comando "upper" -> Transfoma a string letras em maiúscula
frase11 = "Transforma a string em caixa alta"
print(frase11.upper())

# Comando "lower" -> Transforma string em letras minísculas
frase12 = 'Vamos Estudar o Comando "lower"'
print(frase12.lower())

# Comando "capitalize" -> Transforma todos caractres em minúsculo com
# exceção do primeiro caracter da string
frase13 = 'AgorA VamoS EstudaR o ComandO "capitalize"'
print(frase13.capitalize())

# Comando "title" -> Analisa as palavras de uma string e transforma
# a primeira letra de cada palavra em maiúsculo
frase14 = 'Usando o comando "title" em uma string'
print(frase14.title())

# Comando "strip" remove espaços desnecessários no começo e no final
# de uma string
frase15 = '   Removendo espaços desnecessários de uma string      '
print(frase15.strip())

# Comando "rstrip" -> Remove os espaços em branco no final da strin (right)
# Comando "lstrip" -> Remove os espaços em ando no final da string (left)
frase16 = '     Removendo espaços em branco no começo e no final de uma string      '
print(frase16.rstrip())
print(frase16.lstrip())

# Comando "split" --> Divide a string em palavras
# Exemplo: Curso em vídeo Python == Curso | em | Vídeo | Python (cada
# palavra recebe uma indexação nova)
frase17 = 'Estudando o comando split'
print(frase17.split())

# Comando "join" -> Faz a junção de palavras em uma string usando algum caracter
frase18 = 'Juntando frases em uma string'
print('-'.join(frase18))
