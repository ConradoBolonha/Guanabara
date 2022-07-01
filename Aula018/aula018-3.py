'''
pessoa = []
pessoa.append('João')
pessoa.append(25)
caract = []
caract.append(pessoa)
pessoa[0] = 'Maria'
pessoa[1] = 65
caract.append(pessoa)
print(caract)
'''
#  AO EXECUTAR O ALGORITIMO ACIMA, IRÁ MOSTRAR "[['Maria', 65], ['Maria', 65]]", OU SEJA,
#  FEZ UMA LIGAÇÃO ENTRA AS LISTAS "PESSOA" E "CARACT". PARA RESOLVER, PRECISAR USAR O
#  PARÂMETRO "[:]"

pessoa = []
pessoa.append('João')
pessoa.append(25)
caract = []
caract.append(pessoa[:])  #  O PARÂMETRO "[:]" CORTA A LIGAÇÃO ENTRE AS LISTAS
pessoa[0] = 'Maria'
pessoa[1] = 65
caract.append(pessoa[:])
print(caract)
#  [['João', 25], ['Maria', 65]]
